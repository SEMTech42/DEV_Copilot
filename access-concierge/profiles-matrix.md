# Matrice profils → accès

Source de vérité de l'agent. Chaque ligne référence des **access packages Entra** (Entitlement Management) ou des **rôles PIM éligibles** préapprouvés par la sécurité. L'agent ne crée jamais d'accès hors de cette matrice.

> Les identifiants (`AP-…`, `PIM-…`) sont des exemples : remplacez-les par les IDs réels du tenant. À terme, stocker cette matrice dans Dataverse ou une liste SharePoint, et l'exposer à l'agent comme source de connaissance.

## Profils

| Profil | Critères (Entra / RH) | Accès automatiques (sans approbation spécifique) | Accès sur demande (avec approbation) | Rôles privilégiés (PIM, éligibles) |
|---|---|---|---|---|
| `admin-sharepoint` | `jobTitle` contient « Admin SharePoint », département Digital Workplace | AP-M365-BASE, AP-TEAMS-DW | AP-SITE-COLLAB-DW-OWNER, AP-TEAMS-CORPO-COM | PIM-SHAREPOINT-ADMIN (8 h, justification + approbation sécurité) |
| `admin-teams` | `jobTitle` contient « Admin Teams », département Digital Workplace | AP-M365-BASE, AP-TEAMS-DW | AP-TEAMS-CORPO-COM | PIM-TEAMS-ADMIN (8 h, approbation sécurité) |
| `owner-site-collab` | Propriétaire désigné d'un site de collaboration | AP-M365-BASE | AP-SITE-<NOM>-OWNER (approbation propriétaire du site + manager) | aucun |
| `employe-standard` | Tout employé actif | AP-M365-BASE | AP-TEAMS-<EQUIPE>-MEMBER (approbation propriétaire de l'équipe) | aucun |
| `externe` | `userType = Guest` | aucun | AP-GUEST-<PROJET> (approbation sponsor, expiration 90 jours) | interdit |

## Règles transverses

- **Rôle privilégié** : toujours *éligible* (jamais permanent), durée d'activation limitée, justification obligatoire, approbation sécurité.
- **Séparation des tâches** : le demandeur ne peut pas être l'approbateur ; un utilisateur ne peut pas demander un rôle privilégié pour lui-même via l'agent.
- **Expiration** : tout access package non permanent a une date de fin et une revue d'accès (annuelle pour les propriétaires de sites, trimestrielle pour les rôles privilégiés).
- **Profil inconnu ou ambigu** : l'agent ne devine pas, il escalade vers le service IT.
- **Hors matrice** : toute demande qui n'y figure pas est refusée par l'agent et orientée vers le processus manuel.

## Demandeurs autorisés

| Demandeur | Peut demander pour |
|---|---|
| Manager direct | Ses subordonnés directs |
| RH (groupe `GRP-HR-ACCESS-REQUESTERS`) | Tout employé |
| IT (groupe `GRP-IT-ACCESS-OPERATORS`) | Tout utilisateur, hors rôles privilégiés pour soi-même |
