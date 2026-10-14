# Spec : serveur MCP « access-graph »

Petit serveur MCP qui enveloppe les appels Microsoft Graph / Entra nécessaires à Access Concierge. À utiliser si aucun serveur MCP Entra officiel ne couvre ces opérations dans votre tenant. Avantage : on n'expose à l'agent que 6 outils étroits, pas l'API Graph entière.

## Principes

- **Transport** : Streamable HTTP (compatible Copilot Studio et Foundry).
- **Authentification vers Graph** : identité managée ou app registration dédiée, permissions *application* minimales (voir plus bas). Pas de secret dans le code.
- **Authentification de l'appelant** : OAuth/Entra ; l'identité du demandeur est transmise (on-behalf-of) pour que les contrôles d'autorisation s'appuient sur la vraie personne.
- **Aucun outil de lecture ou d'écriture générique** (pas de « call_graph »). Chaque outil valide ses entrées.
- **Idempotence** : `submit_*` accepte un `clientRequestId` ; un même identifiant ne crée pas de doublon.
- **Journal d'audit** de chaque appel (appelant, cible, outil, résultat).

## Outils

### `get_user_profile`
Lit le profil d'un utilisateur.
- Entrée : `userPrincipalName` (string)
- Sortie : `id`, `displayName`, `jobTitle`, `department`, `userType`, `manager { id, displayName }`, `accountEnabled`
- Graph : `GET /users/{id}?$select=…&$expand=manager`

### `check_requester_authorization`
Vérifie qu'un demandeur peut agir pour une cible.
- Entrée : `requesterUpn`, `targetUpn`, `accessCode` (code issu de la matrice)
- Sortie : `{ allowed: boolean, reason: string }`
- Règles : manager direct, membre de `GRP-HR-ACCESS-REQUESTERS` ou `GRP-IT-ACCESS-OPERATORS` ; refus si `requester == target` pour un code privilégié.
- Graph : `GET /users/{id}/manager`, `GET /groups/{id}/members`

### `submit_access_request`
Crée une demande sur un access package.
- Entrée : `targetUpn`, `accessPackageId`, `justification` (string, obligatoire), `clientRequestId`
- Sortie : `requestId`, `state`
- Validation : `accessPackageId` doit figurer dans la liste blanche (matrice) ; sinon rejet.
- Graph : `POST /identityGovernance/entitlementManagement/assignmentRequests` (type `adminAdd`)

### `submit_pim_eligibility_request`
Demande l'éligibilité à un rôle Entra via PIM.
- Entrée : `targetUpn`, `roleDefinitionId`, `justification`, `durationIso8601` (≤ `PT8H` pour l'activation), `clientRequestId`
- Sortie : `requestId`, `state`
- Validation : rôle présent dans la liste blanche ; **toujours éligible, jamais actif ni permanent**.
- Graph : `POST /roleManagement/directory/roleEligibilityScheduleRequests` (action `adminAssign` soumise à approbation selon la politique du rôle)

### `get_request_status`
Suit une demande.
- Entrée : `requestId`
- Sortie : `state` (`pendingApproval` / `approved` / `denied` / `delivered` / `expired`), `currentApprover`, `lastUpdated`
- Graph : `GET /identityGovernance/entitlementManagement/assignmentRequests/{id}` ou `GET /roleManagement/directory/roleEligibilityScheduleRequests/{id}`

### `write_audit_entry`
Écrit une entrée d'audit applicative.
- Entrée : `requesterUpn`, `targetUpn`, `profile`, `requestIds[]`, `summary`
- Sortie : `auditId`
- Cible : table Dataverse ou Log Analytics.

## Permissions Graph (application), à valider avec la sécurité

| Besoin | Permission minimale |
|---|---|
| Lecture profil et manager | `User.ReadBasic.All`, `User.Read.All` (si `jobTitle`/`department`) |
| Appartenance aux groupes | `GroupMember.Read.All` |
| Access packages | `EntitlementManagement.ReadWrite.All` |
| PIM | `RoleEligibilitySchedule.ReadWrite.Directory` |

Préférer des **permissions déléguées / OBO** pour tout ce qui engage le demandeur. Ne jamais accorder `Directory.ReadWrite.All` ni `RoleManagement.ReadWrite.Directory`.

## Structure de projet suggérée

```
mcp-server/
  src/
    server.ts          # enregistrement des outils MCP
    tools/             # un fichier par outil
    graph/client.ts    # client Graph (identité managée)
    policy/allowlist.ts# access packages et rôles autorisés (depuis la matrice)
    audit.ts
  test/                # tests unitaires avec Graph mocké
  Dockerfile
```

## Tests d'acceptation

1. Un `accessPackageId` hors liste blanche est rejeté.
2. Un manager ne peut pas demander un accès pour un utilisateur qui n'est pas son subordonné.
3. Un demandeur ne peut pas demander un rôle privilégié pour lui-même.
4. Deux appels avec le même `clientRequestId` ne créent qu'une demande.
5. Une demande PIM n'est jamais créée en mode actif ou permanent.
6. Chaque appel produit une entrée d'audit.

## Déploiement et branchement

1. Héberger le serveur (Azure Container Apps ou Functions), protégé par Entra.
2. Copilot Studio : *Outils → Ajouter un outil → Model Context Protocol*, saisir l'URL du serveur.
3. Foundry : déclarer l'URL MCP comme outil de l'agent (si vous passez à l'architecture hybride).
