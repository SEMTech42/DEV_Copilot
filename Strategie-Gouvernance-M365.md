# Stratégie de gouvernance Microsoft 365

**Portée :** SharePoint Online, Microsoft Teams, OneDrive, Groupes Microsoft 365, Microsoft Entra ID, Microsoft Purview, Microsoft 365 Copilot
**Auteur :** Architecture Microsoft 365
**Version :** 1.0 — 2026-10-06
**Statut :** Proposition pour validation (comité de gouvernance)

---

## Sommaire

1. Vision et objectifs de gouvernance
2. Contrôle de la création des espaces collaboratifs
3. Catalogue des types d'espaces autorisés
4. Gabarits de sites
5. Gouvernance SharePoint
6. Gouvernance Microsoft Teams
7. Gouvernance OneDrive
8. Gouvernance du partage externe SharePoint
9. Sécurité Microsoft 365
10. Gouvernance Copilot
11. Cycle de vie
12. Matrice RACI
13. Feuille de route de mise en œuvre
14. Décisions de gouvernance recommandées
15. Risques atténués
16. Bénéfices attendus
17. KPIs de suivi
18. Indicateurs de conformité
19. Annexes (commandes de référence, hypothèses)

---

# 1. Vision et objectifs de gouvernance

## 1.1 Pourquoi gouverner Microsoft 365

Microsoft 365 est devenu la plateforme de collaboration et de gestion documentaire de l'organisation, et le socle de données de Copilot. Sans gouvernance, chaque nouvel espace crée une surface d'exposition, un coût de gestion et un risque de non-conformité.

La gouvernance vise à :

- **Protéger l'information** : savoir où sont les données, qui y accède, avec quel niveau de protection.
- **Respecter les obligations légales** : conservation, destruction, accès à l'information, protection des renseignements personnels, exigences sectorielles.
- **Rendre l'information trouvable et fiable** : un espace par besoin, bien nommé, bien classé, sans doublons.
- **Réduire la dette opérationnelle** : moins d'espaces orphelins, moins de permissions héritées ou ad hoc, moins de tickets de support.
- **Préparer Copilot** : Copilot expose ce que l'utilisateur peut déjà lire. La qualité de la gouvernance détermine directement la qualité et la sûreté des réponses.

**Principe directeur : « Libre accès à la collaboration, pas libre création de l'infrastructure. »** On facilite la demande (rapide, standardisée, 1 à 2 jours ouvrables) tout en retirant le droit de créer directement.

## 1.2 Risques du libre-service non contrôlé

| Risque | Description | Conséquence |
|---|---|---|
| Prolifération | Chaque utilisateur crée Teams, Groupes et sites à volonté | Milliers d'espaces dupliqués, peu ou pas utilisés |
| Propriétaires absents | Créateur unique, départ ou changement de poste | Sites orphelins, aucun responsable des accès |
| Nommage incohérent | « Test », « Projet X v2 », « Équipe Marie » | Recherche inefficace, impossibilité de reporting |
| Surpartage | Liens « Anyone », « Organisation entière », permissions uniques | Fuite de données, Copilot qui remonte du contenu non destiné à l'utilisateur |
| Invités non maîtrisés | Invitation directe d'adresses inconnues | Accès externe sans validation ni expiration |
| Absence de classification | Aucune étiquette de sensibilité | DLP et chiffrement inopérants |
| Absence de rétention | Données conservées indéfiniment ou supprimées trop tôt | Non-conformité, risque en litige |
| Données individuelles | Documents corporatifs stockés dans OneDrive | Perte de continuité au départ de l'employé |
| Shadow IT | Contournement par outils tiers | Perte de contrôle totale |

## 1.3 Enjeux de la multiplication des sites, Teams et Groupes

- **Un Team = un Groupe M365 = un site SharePoint** (plus Planner, boîte partagée, calendrier, etc.). Une création anodine déclenche donc 4 à 6 objets à gouverner.
- **Les canaux** génèrent des dossiers, et les canaux privés/partagés des **sites SharePoint supplémentaires** avec permissions propres.
- **Coût de stockage** : quotas, sauvegarde, restauration.
- **Charge d'audit** : plus il y a d'espaces, plus les revues d'accès sont longues et moins elles sont faites.
- **Limites techniques** : plafonds de tenant, performance de la recherche, lisibilité des listes de Groupes dans l'annuaire.

## 1.4 Impacts

**Sécurité**
- Surface d'attaque élargie, comptes compromis ayant accès à de nombreux espaces.
- Partage externe incontrôlé, liens persistants.

**Conformité**
- Impossible d'appliquer de façon cohérente rétention, étiquettes et eDiscovery.
- Difficulté à répondre à une demande d'accès à l'information ou à un litige.

**Recherche d'information**
- Résultats bruités : versions multiples, brouillons, espaces abandonnés.
- Perte de confiance dans la « version officielle ».

**Copilot**
- Copilot utilise Microsoft Graph et respecte les permissions, mais **il rend visible instantanément ce qui était « caché par obscurité »**.
- Un site mal protégé, un lien « organisation entière » ou un groupe trop large devient une source de réponses.
- Du contenu obsolète ou dupliqué dégrade la pertinence des réponses (hallucinations de contexte, informations périmées).
- Risque de fuite involontaire d'informations sensibles (RH, finance, juridique) dans les résumés générés.

## 1.5 Objectifs mesurables de gouvernance

| # | Objectif | Cible |
|---|---|---|
| O1 | 100 % des espaces créés via le portail | 100 % à la fin de la phase 2 |
| O2 | 100 % des sites avec ≥ 2 propriétaires actifs | ≥ 98 % |
| O3 | 0 lien anonyme / « Anyone » | 0 |
| O4 | Sites étiquetés (sensibilité) | ≥ 95 % |
| O5 | Délai de provisioning | ≤ 2 jours ouvrables (≤ 4 h après approbations) |
| O6 | Sites inactifs > 12 mois archivés ou supprimés | ≥ 95 % traités |
| O7 | Revue d'accès annuelle complétée | ≥ 95 % |
| O8 | Éléments de surpartage corrigés avant Copilot | 100 % des sites critiques |

---

# 2. Contrôle de la création des espaces collaboratifs

## 2.1 Principe

Les utilisateurs **ne peuvent plus** créer directement :

- des **Groupes Microsoft 365** (Outlook, Planner, Viva Engage, Teams, Power BI, Stream, Forms, etc.) ;
- des **sites SharePoint** (Équipe, Communication) ;
- des **Teams**.

Toute création passe par un **portail TI**, avec workflow d'approbation et provisioning automatisé.

## 2.2 Mesures techniques de blocage

### a) Restreindre la création de Groupes M365 (Entra ID)

1. Créer un groupe de sécurité Entra ID : `SG-M365-GroupCreators` (membres : comptes de service du provisioning et équipe TI M365).
2. Appliquer le paramètre d'annuaire « Group.Unified » :
   - `EnableGroupCreation = False`
   - `GroupCreationAllowedGroupId = <ObjectId de SG-M365-GroupCreators>`
3. Définir `UsageGuidelinesUrl` vers la page d'aide du portail et `CustomBlockedWordsList` pour interdire des mots réservés (ex. « test », « temp »).

Ce paramètre bloque la création depuis Outlook, Teams, Planner, SharePoint, Viva Engage, Stream, Forms, Bookings, To Do, Power BI, Project.

> Note : Un administrateur (rôle Global Admin, Groups Admin, SharePoint Admin, Teams Admin, User Admin) contourne cette restriction. Limiter ces rôles avec PIM.

### b) Restreindre la création de sites SharePoint

- Centre d'administration SharePoint → Paramètres → **Création de sites** : désactiver la création de sites par les utilisateurs (« Site creation »).
- **SharePoint Advanced Management (SAM)** : utiliser la fonctionnalité de gestion de la création de sites et les politiques de sites si licenciées.
- Désactiver le « Créer un site » dans la page d'accueil SharePoint et la création de sites depuis la liste de fichiers.
- Rediriger vers le portail avec une URL de création personnalisée (`SPO tenant: SiteCreationDefaultManagedPath`, `CustomizedExternalSharingServiceUrl`) et le message d'aide.

### c) Restreindre la création de Teams

- Découle du blocage des Groupes M365 (un Team nécessite un Groupe).
- Complémentaire : stratégies Teams (`Set-CsTeamsChannelsPolicy`) pour limiter les canaux privés/partagés, et stratégies d'application pour limiter les apps de création.

### d) Fermer les contournements

| Voie de contournement | Contrôle |
|---|---|
| Power Automate / Graph via utilisateurs | DLP Power Platform + restriction des connecteurs de création de groupes |
| PowerShell / PnP par utilisateurs | Pas de rôle admin ; revue PIM ; audit Purview |
| Formulaires Forms / Planner / Bookings | Bloqués via paramètre Groupe |
| Sites OneDrive | Hors périmètre de la création de sites (propre à chaque utilisateur) ; partage externe désactivé (section 7) |
| Sites de communication « modernes » | Désactivation de la création en libre-service SPO |
| Sous-sites | Désactivation de la création de sous-sites (« Subsite creation » désactivé, architecture plate avec Hubs) |
| Wikis, Loop | Contrôle des espaces Loop (Loop workspaces) et des composants |

## 2.3 Le portail TI

### Option A — Power Apps + Power Automate (recommandée si l'écosystème est Microsoft)

- **Power Apps (canvas ou model-driven)** : formulaire de demande avec choix du type d'espace, justification, propriétaires, sensibilité, invités externes (oui/non), date de fin (projet).
- **Dataverse** (ou liste SharePoint dédiée) comme registre de demandes et **registre des espaces** (source de vérité du cycle de vie).
- **Power Automate** : orchestration (approbations, vérifications, appel Graph, notifications).
- **Approvals** : approbation gestionnaire, validation TI, validation sécurité.
- **Teams / Outlook** : cartes adaptatives pour les approbateurs.

### Option B — ServiceNow

- Catalogue de services « Espace collaboratif M365 » avec variables de formulaire.
- Flow Designer / Workflow Studio pour approbations (gestionnaire, TI, sécurité).
- **IntegrationHub / Spoke Microsoft Graph** ou appel REST vers une **Azure Function** / **Power Automate HTTP** qui exécute le provisioning.
- Avantage : processus ITSM existant, CMDB, SLA, reporting. À privilégier si ServiceNow est déjà le point d'entrée TI.

### Principes communs

- Une **seule porte d'entrée** (lien unique, intégré à la page d'accueil SharePoint, Teams, intranet).
- Authentification Entra ID, formulaire pré-rempli (nom, direction, gestionnaire via Graph).
- **Idempotence** et **journalisation** de chaque étape.
- Exécution du provisioning par une **identité applicative (App Registration / Managed Identity)** avec permissions minimales (principe du moindre privilège), jamais par un compte humain.

## 2.4 Processus complet

```
Demande → Approbation → Vérification → Création → Attribution des propriétaires → Notification
```

### Étape 1 — Demande

Le demandeur remplit le formulaire :

| Champ | Détail |
|---|---|
| Type d'espace | Équipe / Projet / Communication / Communauté / Extranet |
| Nom proposé | Validé selon la convention de nommage (aperçu en direct) |
| Description et finalité | Texte libre (min. 100 caractères) |
| Direction / unité | Liste (alimente préfixe et Hub) |
| Propriétaires | ≥ 2 (le demandeur + 1 co-propriétaire) |
| Membres initiaux | Optionnel |
| Teams requis | Oui / Non |
| Sensibilité estimée | Général / Interne / Confidentiel / Hautement confidentiel |
| Invités externes | Oui / Non (si oui : organisation, justification, durée) |
| Date de fin | Obligatoire pour Projet |
| Gestionnaire approbateur | Pré-rempli depuis Entra ID (`manager`) |

Contrôles immédiats dans le formulaire : doublons de nom, mots interdits, propriétaires valides (comptes actifs, internes), cohérence type/sensibilité.

### Étape 2 — Approbation

1. **Approbation du gestionnaire** du demandeur (ou du responsable de direction pour une Équipe) — pertinence métier et budget.
2. **Validation TI (Gouvernance M365)** — conformité au catalogue, absence de doublon, choix du gabarit, capacité.
3. **Validation Sécurité** — **obligatoire** si :
   - type **Extranet** ;
   - présence d'invités externes ;
   - sensibilité **Confidentiel** ou plus ;
   - données réglementées (renseignements personnels, santé, finance) ;
   - demande de dérogation à un gabarit.

SLA : 2 jours ouvrables par étape, rappel automatique à 24 h, escalade au gestionnaire de l'approbateur à 48 h. Refus : motif obligatoire retourné au demandeur.

### Étape 3 — Vérification

Contrôles automatisés avant création :

- Nom unique (SharePoint URL + `displayName` du Groupe + alias).
- Conformité à la convention de nommage.
- Propriétaires : ≥ 2, actifs, licenciés, pas de comptes invités, pas de comptes de service.
- Gabarit compatible avec le type et la sensibilité.
- Date de fin présente (Projet) et ≤ 24 mois.
- Pour Extranet : approbation sécurité horodatée, liste d'invités pré-validée.
- Capacité tenant (quotas).

Échec → retour au demandeur avec message précis.

### Étape 4 — Création (automatisée via Microsoft Graph)

Exécutée par une **App Registration** (certificat ou Managed Identity) avec permissions applicatives limitées (`Group.Create`, `Sites.FullControl.All` ou, de préférence, **`Sites.Selected`** + `Team.Create`, `TeamSettings.ReadWrite.All`, `Directory.ReadWrite.All` au strict nécessaire).

Séquence type :

1. `POST /groups` — Groupe M365 (`groupTypes: ["Unified"]`, `visibility: Private`, `resourceBehaviorOptions`, propriétaires inclus à la création) avec étiquette de sensibilité (`assignedLabels`).
2. Attente de propagation du site (`GET /groups/{id}/sites/root`).
3. `PUT /groups/{id}/team` — création du Team (si requis) avec modèle approuvé.
4. Appel **PnP Provisioning / Site Script / Graph** : application du **gabarit** (bibliothèques, types de contenu, métadonnées, navigation, branding, permissions).
5. Association au **Hub** (`Add-PnPHubSiteAssociation` / API Hub).
6. Application de l'**étiquette de sensibilité** et de la **politique de rétention** (via étiquette ou politique Purview ciblant le site).
7. Enregistrement au **registre des espaces** (ID Groupe, URL, type, propriétaires, date de création, date de fin, sensibilité).
8. Pour **Communication** : création via SharePoint REST/`Add-PnPSiteCommunicationSite` (site sans Groupe) avec 2 propriétaires.

Gestion d'erreurs : reprise (retry exponentiel), compensation (suppression de ressources partielles), alerte à l'équipe TI.

### Étape 5 — Attribution des propriétaires

- Propriétaires ajoutés **à la création** du Groupe (évite l'orphelin) puis confirmés (≥ 2).
- Groupe de sécurité des **propriétaires de secours** de la direction ajouté comme propriétaire de site (admin de collection) pour les sites Équipe/Projet critiques.
- Propriétaires inscrits au registre ; premier **accusé de responsabilités** (acceptation électronique du rôle de propriétaire et du guide de bonnes pratiques).
- Rôle du propriétaire : gérer les membres, répondre aux revues d'accès, signaler l'activité.

### Étape 6 — Notification

| Destinataire | Message |
|---|---|
| Demandeur et propriétaires | Lien du site/Team, guide de démarrage, rappel des responsabilités et de la date de revue |
| Gestionnaire | Confirmation de la création |
| Équipe sécurité | (Extranet / confidentiel) fiche de création |
| Équipe TI | Entrée au registre, tableau de bord |
| Refus | Motif + piste alternative (réutiliser un espace existant) |

Notifications par Teams (carte adaptative) et courriel. Une **vérification à J+30** s'assure que l'espace est utilisé et que les propriétaires ont pris connaissance de leur rôle.

## 2.5 Schéma de flux

```
[Utilisateur] → [Portail Power Apps / ServiceNow]
       ↓
[Contrôles de validation immédiats]
       ↓
[Approbation gestionnaire] → refus → [Notification refus]
       ↓
[Validation TI] → refus → [Notification refus]
       ↓
[Validation Sécurité si requis] → refus → [Notification refus]
       ↓
[Vérifications automatisées]
       ↓
[Graph : Groupe → Site → Team → Gabarit → Hub → Étiquette → Rétention]
       ↓
[Registre des espaces] → [Propriétaires confirmés] → [Notification]
```

## 2.6 Exemple d'appel Graph (création du Groupe)

```http
POST https://graph.microsoft.com/v1.0/groups
Content-Type: application/json

{
  "displayName": "EQ-RH-Recrutement",
  "description": "Espace d'équipe - Direction RH - Recrutement",
  "mailNickname": "eq-rh-recrutement",
  "groupTypes": ["Unified"],
  "mailEnabled": true,
  "securityEnabled": false,
  "visibility": "Private",
  "owners@odata.bind": [
    "https://graph.microsoft.com/v1.0/users/<owner1-id>",
    "https://graph.microsoft.com/v1.0/users/<owner2-id>"
  ],
  "assignedLabels": [ { "labelId": "<guid-etiquette-interne>" } ]
}
```

---

# 3. Catalogue des types d'espaces autorisés

Seuls ces cinq types peuvent être demandés. Toute autre demande est traitée comme une **dérogation** (validation TI + sécurité).

## 3.1 Vue d'ensemble

| Critère | Équipe | Projet | Communication | Communauté de pratique | Extranet |
|---|---|---|---|---|---|
| Durée | Permanente | Temporaire | Permanente | Permanente | Selon entente |
| Technologie | Groupe M365 + site d'équipe (+ Teams) | Groupe M365 + site d'équipe (+ Teams) | Site de communication (sans Groupe) | Site de communication ou Équipe + Viva Engage | Groupe M365 + site d'équipe dédié |
| Visibilité | Privée | Privée | Lecture large, édition restreinte | Ouverte aux internes (lecture) | Privée, invités nommés |
| Membres | Internes | Internes (invités sur approbation) | Lecteurs : organisation / ciblés | Internes | Internes + invités Entra ID approuvés |
| Date de fin | Non | **Obligatoire** | Non | Non | Obligatoire (expiration de l'entente) |
| Approbation | Gestionnaire + TI | Gestionnaire + TI | Gestionnaire + TI | Gestionnaire + TI | Gestionnaire + TI + **Sécurité** |
| Revue | Annuelle | Semestrielle + fin de projet | Annuelle | Annuelle | Trimestrielle |
| Sensibilité par défaut | Interne | Interne | Général / Interne | Interne | Confidentiel |

## 3.2 Site Équipe

**Usage**
- Collaboration permanente d'une direction ou d'un service.
- Gestion documentaire courante.
- Teams associé (optionnel mais recommandé).

**Caractéristiques**
- **Site privé** (visibilité du Groupe : Private).
- **Membres internes uniquement** (pas d'invités par défaut).
- 2 propriétaires minimum, membres gérés via le groupe M365.
- Associé au Hub de la direction.
- Étiquette de sensibilité par défaut : *Interne* (relevable à *Confidentiel*).
- Pas de sous-sites ; structure par bibliothèques et dossiers limités à 3 niveaux.

## 3.3 Site Projet

**Usage**
- Projet à durée limitée.
- Équipe multidisciplinaire (plusieurs directions).

**Caractéristiques**
- **Date de fin obligatoire** (maximum 24 mois, prolongeable sur approbation).
- **Révision périodique** : tous les 6 mois, plus revue de clôture.
- À l'échéance : propriétaires notifiés 60, 30 et 7 jours avant ; passage en **lecture seule**, puis archivage (voir section 11).
- Gabarit incluant registre des risques, livrables, décisions, jalons.
- Membres hors direction autorisés (internes). Invités externes seulement avec validation sécurité.

## 3.4 Site Communication

**Usage**
- Diffusion d'information.
- Portail départemental ou corporatif.

**Caractéristiques**
- **Peu de contributeurs** (2 à 10 éditeurs nommés) et **beaucoup de lecteurs** (groupe « Visiteurs » : tous les employés ou groupe ciblé).
- Pas de Groupe M365 (site de communication autonome) : permissions gérées par groupes Entra ID de sécurité.
- Pages approuvées (flux d'approbation de pages, publication planifiée).
- Contenu réputé « publié » : pas de documents de travail ; versions finales uniquement.
- Étiquette *Général* ou *Interne*. Aucun contenu confidentiel.

## 3.5 Site Communauté de pratique

**Usage**
- Partage de connaissances entre pairs, transversal aux directions.

**Caractéristiques**
- Rattaché à un domaine d'expertise (ex. Analyse de données, Gestion de projet, Cybersécurité).
- Animateur (propriétaire) + co-animateur obligatoire.
- Composantes : bibliothèque de ressources, FAQ, calendrier d'événements, canal Teams ou communauté Viva Engage (selon usage).
- Lecture ouverte aux internes, contribution par inscription.
- Étiquette *Interne*. Pas de données confidentielles.
- Revue annuelle d'activité : sans activité sur 12 mois → archivage.

## 3.6 Site Extranet

**Usage**
- Collaboration avec partenaires, fournisseurs ou clients externes.

**Caractéristiques**
- **Approbation sécurité obligatoire** avant création.
- **Gouvernance renforcée** :
  - site dédié, aucun partage avec des espaces internes ;
  - invités **uniquement** comptes Entra ID (B2B) validés ;
  - étiquette de sensibilité *Confidentiel – Externe* (restrictions de téléchargement, chiffrement, filtrage d'accès non géré) ;
  - accès conditionnel dédié aux invités (MFA, appareil conforme ou navigateur seulement) ;
  - **expiration automatique** des invités (90 jours renouvelables) ;
  - revue trimestrielle des accès par les propriétaires ;
  - date de fin liée à l'entente contractuelle ;
  - journalisation renforcée et alertes Purview.
- Documents sensibles : exclus par défaut (DLP bloquant le partage de contenu étiqueté *Hautement confidentiel*).

---

# 4. Gabarits de sites

## 4.1 Approche de provisioning

Chaque type d'espace correspond à un **gabarit standard** maintenu comme code (Infrastructure as Code) :

- **PnP Provisioning Templates** (XML/YAML) + **SharePoint Site Designs/Site Scripts** pour la structure.
- **Graph / PowerShell** pour Groupe, Team, étiquettes, rétention.
- Dépôt Git versionné (Azure DevOps ou GitHub), revue de code, tests dans un tenant de développement, déploiement par pipeline CI/CD.
- **Catalogue de gabarits versionné** (v1.0, v1.1…) : une évolution est appliquée aux nouveaux sites et, par vague contrôlée, aux sites existants.
- Aucune configuration manuelle post-création, sauf contenu métier.

## 4.2 Éléments communs à tous les gabarits

- Thème et branding corporatifs (thème de site, logo, en-tête compact, pied de page).
- Association au **Hub** de la direction.
- Étiquette de sensibilité et politique de rétention appliquées à la création.
- Désactivation du partage « Tout le monde » et des liens anonymes.
- Partage limité aux « personnes ayant déjà accès » ou « personnes spécifiques » (internes) ; invités selon le type.
- Versionnage activé (majeur, 100 versions), corbeille activée.
- Colonnes de site obligatoires (section 5.5).
- Audit activé, enregistrement dans le registre.

## 4.3 Gabarit « Équipe »

| Élément | Configuration |
|---|---|
| **Bibliothèques** | Documents (par défaut, renommée « Documents de l'équipe »), Procédures et politiques, Comptes rendus de réunions, Archives (lecture seule) |
| **Métadonnées obligatoires** | Direction, Type de document, Statut (Brouillon / En révision / Approuvé / Archivé), Propriétaire du document, Classification |
| **Étiquette de sensibilité** | *Interne* par défaut ; *Confidentiel* disponible |
| **Rétention** | Politique « Documents d'équipe » : conserver 7 ans après dernière modification puis révision (à valider avec la gestion documentaire) ; Teams chat/canal : 3 ans |
| **Groupes de permissions** | Propriétaires (Contrôle total), Membres (Modifier), Visiteurs (Lecture, optionnel). Pas de permissions uniques sans justification |
| **Navigation** | Navigation du Hub + navigation locale : Accueil, Documents, Procédures, Réunions, Archives |
| **Branding** | Thème corporatif, bannière direction, logo, pied de page avec contact du propriétaire |

## 4.4 Gabarit « Projet »

| Élément | Configuration |
|---|---|
| **Bibliothèques** | Livrables, Gestion de projet (charte, plan, jalons), Décisions et comptes rendus, Documents de référence, Archives |
| **Listes** | Registre des risques, Registre des enjeux, Registre des décisions, Jalons |
| **Métadonnées obligatoires** | N° de projet, Phase (Initiation / Planification / Exécution / Clôture), Type de document, Statut, Confidentialité |
| **Étiquette de sensibilité** | *Interne* par défaut ; *Confidentiel* selon le projet |
| **Rétention** | Étiquette de rétention de **clôture de projet** : déclenchement à la date de fin ; conservation 5 à 7 ans selon l'étiquette, puis révision de disposition |
| **Groupes de permissions** | Sponsor (Lecture), Chargé de projet (Propriétaire), Équipe (Modifier), Parties prenantes (Lecture) |
| **Navigation** | Accueil, Livrables, Gestion, Risques/Enjeux, Décisions, Archives |
| **Branding** | Thème corporatif + bandeau « Projet – date de fin : AAAA-MM-JJ » |
| **Spécifique** | Colonne/propriété *Date de fin* du site ; flux de notification d'échéance (60/30/7 jours) |

## 4.5 Gabarit « Communication »

| Élément | Configuration |
|---|---|
| **Bibliothèques** | Pages du site, Ressources de pages (images, vidéos), Documents publiés (lecture seule pour visiteurs) |
| **Métadonnées obligatoires** | Catégorie de page, Date de publication, Date de révision, Auteur responsable, Public cible |
| **Étiquette de sensibilité** | *Général* ou *Interne* |
| **Rétention** | Pages : révision annuelle, suppression si non modifiées 3 ans (après avis) ; ressources : 5 ans |
| **Groupes de permissions** | Propriétaires (Contrôle total), Éditeurs (Modifier, 2-10 personnes), Visiteurs (Lecture : tous ou groupe ciblé) |
| **Navigation** | Navigation en en-tête (méga-menu), liens vers Hub, actualités, outils |
| **Branding** | Thème corporatif complet, page d'accueil modèle avec section « Nouvelles », « Liens rapides », « Contacts » |
| **Spécifique** | Approbation de pages activée ; publication planifiée ; rôle de publicateur distinct |

## 4.6 Gabarit « Communauté de pratique »

| Élément | Configuration |
|---|---|
| **Bibliothèques** | Ressources et bonnes pratiques, Présentations et webinaires, Gabarits partagés |
| **Listes** | FAQ, Calendrier d'événements, Annuaire des membres/experts |
| **Métadonnées obligatoires** | Thème, Type de ressource, Niveau (Débutant / Intermédiaire / Expert), Auteur |
| **Étiquette de sensibilité** | *Interne* |
| **Rétention** | 3 ans après dernière modification, révision annuelle par l'animateur |
| **Groupes de permissions** | Animateurs (Propriétaires), Contributeurs (Modifier), Membres (Lecture) |
| **Navigation** | Accueil, Ressources, FAQ, Événements, Experts |
| **Branding** | Thème corporatif + identité de la communauté (icône, couleur d'accent limitée) |
| **Spécifique** | Canal Teams ou communauté Viva Engage selon le choix à la demande |

## 4.7 Gabarit « Extranet »

| Élément | Configuration |
|---|---|
| **Bibliothèques** | Documents partagés avec partenaire, Livrables du partenaire, Documents contractuels (accès restreint) |
| **Métadonnées obligatoires** | Partenaire, Entente/Contrat, Type de document, Statut, Classification |
| **Étiquette de sensibilité** | *Confidentiel – Externe* (obligatoire, non modifiable par l'utilisateur) |
| **Rétention** | Alignée sur la durée de l'entente + 7 ans ; invités expirés à la fin |
| **Groupes de permissions** | Propriétaires internes (Contrôle total), Membres internes (Modifier), Invités partenaires (Lecture ou Modifier selon bibliothèque), **jamais Contrôle total** |
| **Navigation** | Navigation minimale, aucune exposition du Hub interne |
| **Branding** | Thème neutre corporatif, bandeau « Espace partagé avec des partenaires externes – ne pas déposer d'information classifiée » |
| **Spécifique** | Désactivation du téléchargement sur appareils non gérés (accès conditionnel session), recherche limitée au site, **non associé** à un Hub interne, filtrage de la recherche pour exclure ce site de Copilot interne si requis |

## 4.8 Pourquoi les gabarits ?

| Bénéfice | Explication |
|---|---|
| **Standardisation** | Même structure, mêmes noms de bibliothèques, mêmes colonnes : les utilisateurs savent où chercher, la recherche et les vues transversales fonctionnent |
| **Gouvernance** | Sécurité, rétention, étiquettes et audit sont appliqués **dès la naissance** du site, pas « plus tard » ; la conformité est par conception |
| **Adoption** | Un espace prêt à l'emploi, avec structure logique, réduit la friction ; les utilisateurs n'ont plus à « concevoir » leur site |
| **Réduction des risques** | Disparition des permissions improvisées, du surpartage, des sites sans propriétaires, des configurations oubliées ; les évolutions de sécurité sont déployées centralement |
| **Efficacité TI** | Provisioning en minutes, coût de support réduit, tests reproductibles |
| **Qualité pour Copilot** | Métadonnées cohérentes, contenu classé, sources identifiables : réponses plus pertinentes |

---

# 5. Gouvernance SharePoint

## 5.1 Convention de nommage

**Format général :** `[Type]-[Direction]-[Nom descriptif]`

| Type | Préfixe | Exemple (titre) | URL |
|---|---|---|---|
| Équipe | `EQ` | EQ-RH-Recrutement | `/sites/eq-rh-recrutement` |
| Projet | `PRJ` | PRJ-2026-045-Migration ERP | `/sites/prj-2026-045-migration-erp` |
| Communication | `COM` | COM-Finance-Portail | `/sites/com-finance-portail` |
| Communauté | `CDP` | CDP-Analyse de données | `/sites/cdp-analyse-donnees` |
| Extranet | `EXT` | EXT-Fournisseur X-Entente 2026 | `/sites/ext-fournisseur-x-2026` |

Règles :

- Pas d'accents, d'espaces ni de caractères spéciaux dans l'URL ; minuscules.
- Longueur maximale 60 caractères pour le titre.
- Pas de noms de personnes, pas de « test », « nouveau », « v2 », « final ».
- Nom unique, vérifié par le portail.
- **Politique de nommage des Groupes Entra ID** (Group naming policy) : préfixe obligatoire et liste de mots bloqués, en complément de la validation du portail.
- Teams : même nom que le site (voir section 6).
- Renommage : uniquement via une demande de modification (conservation de l'historique dans le registre).

## 5.2 Gestion des propriétaires

- **Minimum 2 propriétaires actifs par site**, internes, avec licence.
- Le portail refuse la création avec moins de 2 propriétaires.
- **Contrôle mensuel automatisé** (Power Automate / script Graph) : sites avec < 2 propriétaires actifs → alerte au propriétaire restant et au gestionnaire ; escalade à la TI après 14 jours.
- Les départs (flux RH / Entra ID `accountEnabled = false`) déclenchent la réaffectation.
- Propriétaire de secours : groupe de gouvernance de la direction.
- Les propriétaires acceptent un **guide de responsabilités** (gestion des accès, respect de la classification, réponse aux revues).
- Les propriétaires ne sont **pas** des invités ni des comptes de service.

## 5.3 Révision annuelle des accès

- **Entra ID Access Reviews** (Groupes M365) : cycle annuel pour les sites Équipe, Communication, Communauté ; **semestriel** pour Projet ; **trimestriel** pour Extranet et sites confidentiels.
- Réviseurs : propriétaires du site (fallback : gestionnaire de direction).
- Décision par défaut en l'absence de réponse : **retrait** de l'accès pour les invités, **maintien + escalade** pour les internes.
- Les résultats sont archivés (preuve d'audit) dans Purview / Entra.
- SharePoint : rapport « Accès au site » (SAM — **Site Access Review**) pour les sites non basés sur Groupes (communication) et pour les permissions uniques.

## 5.4 Sites orphelins

**Définition :** site sans propriétaire actif ou avec moins de 2 propriétaires actifs.

Traitement :

1. Détection hebdomadaire (Graph : propriétaires du Groupe ; SharePoint Admin : administrateurs de collection).
2. Notification au gestionnaire du dernier propriétaire connu et aux membres.
3. Délai de 14 jours pour désigner un propriétaire.
4. À défaut : TI assigne le propriétaire de secours de la direction ; si aucune direction ne le réclame sous 30 jours, le site passe en lecture seule puis dans le processus d'archivage.
5. Politique **Entra ID Groups Expiration** (renouvellement) comme filet de sécurité supplémentaire.

## 5.5 Archivage

- Critères : aucune activité (modifications/consultations) depuis **12 mois** (SAM : *Inactive sites policy*), fin de projet, décision du propriétaire.
- Étapes : notification (30 jours) → lecture seule (`SetLockState ReadOnly`) → archivage (**Microsoft 365 Archive** pour SharePoint si disponible, sinon export + conservation) → conservation selon rétention.
- Sites archivés exclus de la recherche par défaut (et de Copilot), restaurables par la TI sur demande.

## 5.6 Suppression automatisée des sites inactifs

- **SAM — Inactive sites policy** : détection automatique, courriel aux propriétaires, action par défaut.
- Chaîne : inactif 12 mois → avis → lecture seule à 13 mois → suppression à 18 mois (vers corbeille de collection de sites, restaurable **93 jours**).
- Exceptions : gel légal (Purview eDiscovery/Hold), sites sous rétention, sites de conformité, liste blanche approuvée.
- Une **politique de rétention Purview** peut empêcher la suppression effective : la conformité prime.
- Chaque suppression est journalisée au registre.

## 5.7 Sites Hub

- Un **Hub par direction** (ex. Hub RH, Hub Finance) + Hubs transversaux (Projets, Communautés de pratique, Corporatif).
- Rôle : navigation partagée, thème commun, recherche étendue, agrégation de nouvelles/documents.
- **Le Hub n'accorde pas de permissions** : il ne remplace pas la gouvernance des accès.
- Seul le propriétaire du Hub (TI + direction) approuve l'association (**Hub join approval** activée).
- Architecture **plate** : sites associés à un Hub, pas de sous-sites.
- Hub Extranet : aucun (les sites Extranet ne sont pas associés aux Hubs internes).

## 5.8 Architecture d'information

```
Corporatif (Hub Corporatif — Communication)
 ├─ Hub Direction A
 │   ├─ Site Équipe A1 (Teams)
 │   ├─ Site Communication A (portail)
 │   └─ Sites Projets de la direction
 ├─ Hub Direction B
 │   └─ ...
 ├─ Hub Projets transversaux
 ├─ Hub Communautés de pratique
 └─ Extranet (non associé aux Hubs)
```

- Taxonomie d'entreprise (Term Store) : Directions, Types de documents, Statuts, Thèmes.
- Séparation claire : **contenu publié** (Communication) vs **contenu de travail** (Équipe/Projet) vs **contenu officiel/enregistrements** (bibliothèque/centre de documents avec rétention).
- Principe : « un document, un emplacement » ; liens plutôt que copies.

## 5.9 Métadonnées obligatoires

| Colonne | Type | Valeurs / Source |
|---|---|---|
| Direction | Choix géré (Term Store) | Liste des directions |
| Type de document | Choix géré | Politique, Procédure, Rapport, Compte rendu, Contrat, Gabarit, Autre |
| Statut | Choix | Brouillon, En révision, Approuvé, Archivé |
| Propriétaire du document | Personne | Utilisateur interne |
| Classification | Choix / Étiquette de sensibilité | Alignée sur Purview |
| Date de révision | Date | Pour les documents officiels |

- Colonnes **obligatoires** dans les bibliothèques de gabarit ; valeurs par défaut au niveau du dossier/bibliothèque pour limiter la saisie.
- Métadonnées de **site** : Type d'espace, Direction, Date de fin, Sensibilité, Propriétaires (registre central).

## 5.10 Types de contenu

- **Hub de types de contenu** (Content Type Gallery) publié centralement : modifications propagées aux sites.
- Types de base : Document corporatif, Politique/Procédure, Compte rendu, Livrable de projet, Contrat, Page d'actualité.
- Chaque type porte : colonnes, modèle de document, flux, étiquette de rétention suggérée.
- Création de types de contenu locaux interdite (sauf dérogation).

## 5.11 Gestion documentaire

- **Versionnage** : versions majeures/mineures pour les documents officiels, limite de 100 versions (réduction du stockage).
- **Extraction obligatoire** désactivée (co-édition), approbation de contenu pour les documents officiels.
- **Nommage des fichiers** : guide (date ISO, sujet, version), pas d'obligation technique.
- **Vues standard** : Par statut, Par propriétaire, Par date de révision.
- **Co-édition** : privilégier les liens (pas de pièces jointes).
- **Documents officiels / enregistrements** : étiquette de rétention déclarant l'enregistrement (immuable si requis).
- **Limites de profondeur** de dossiers (≤ 3 niveaux), préférence aux métadonnées.
- **Ménage** : revue annuelle du contenu ROT (redondant, obsolète, trivial) par le propriétaire.

---

# 6. Gouvernance Microsoft Teams

## 6.1 Modèles Teams approuvés

Modèles Teams (Teams templates) personnalisés, **seule source** de création :

| Modèle | Usage | Canaux préconfigurés |
|---|---|---|
| **Équipe de direction/service** | Collaboration permanente | Général, Annonces, Opérations, Réunions |
| **Projet** | Projet temporaire | Général, Planification, Livrables, Risques et enjeux, Réunions |
| **Communauté de pratique** | Partage de connaissances | Général, Questions/Réponses, Ressources, Événements |
| **Extranet / Partenaire** | Collaboration externe | Général, Échanges avec partenaire (canal partagé selon besoin) |

- Les modèles intègrent onglets (SharePoint, Planner, OneNote), paramètres des membres (création de canaux, applications, mentions) et étiquette de sensibilité.
- Les modèles sont revus **semestriellement** par le comité de gouvernance.

## 6.2 Contrôle de création de Teams

- Aucune création directe par l'utilisateur (blocage de la création de Groupes M365, section 2).
- Création uniquement via le portail (Graph : `PUT /groups/{id}/team` ou `POST /teams` avec modèle).
- **Un Team doit être rattaché à un type d'espace du catalogue.**
- Pas de Teams « sans site » : toute équipe correspond à un site gouverné.
- Stratégies d'applications Teams : liste d'applications approuvées uniquement ; applications tierces par approbation TI.

## 6.3 Nommage

- Même nom que le site SharePoint : `EQ-RH-Recrutement`, `PRJ-2026-045-Migration ERP`.
- Politique de nommage de Groupe Entra (préfixe, mots bloqués).
- Canaux : noms courts, sans identifiants confidentiels ; canaux standards dictés par le modèle.
- Aucune équipe nommée d'après une personne.

## 6.4 Propriétaires multiples

- **≥ 2 propriétaires** (même règle que SharePoint, partagés car Groupe M365 commun).
- Les propriétaires gèrent les membres, les canaux privés, les invités approuvés.
- Alerte automatique si un seul propriétaire reste.
- Ratio recommandé : 1 propriétaire pour ≤ 25 membres, max 10 propriétaires.

## 6.5 Gestion des invités

- Aucun accès invité par défaut dans un Team interne.
- Invités **uniquement** comptes Entra ID B2B préapprouvés (section 8).
- L'ajout d'un invité à un Team interne nécessite la validation TI (portail) ; Extranet : validation sécurité.
- Paramètres invités restrictifs (pas de création/suppression de canaux, pas de téléversement non nécessaire).
- Étiquette de sensibilité qui contrôle l'accès des invités (`AllowGuestAccess` selon l'étiquette).
- Revue trimestrielle des invités (Access Reviews).
- **Accès conditionnel** spécifique aux invités.

## 6.6 Archivage des équipes inactives

- Détection : aucune activité (messages, fichiers, réunions) depuis **6 mois** (rapports d'activité Teams / Graph).
- Notification aux propriétaires (30 jours) → archivage (`POST /teams/{id}/archive` : lecture seule, site SharePoint en lecture seule) → suppression du Groupe selon rétention.
- Désarchivage sur demande du propriétaire via portail.
- Les Teams de projet sont archivés automatiquement à la date de fin.

## 6.7 Cycle de vie des Teams

```
Demande → Approbation → Création (modèle) → Utilisation active
→ Revue (annuelle / semestrielle) → Inactivité détectée → Archivage
→ Rétention → Suppression (Groupe + site)
```

- **Expiration du Groupe M365** (Entra ID) : 365 jours, renouvellement automatique si activité, sinon notification aux propriétaires (30, 15, 1 jour) ; suppression logique restaurable 30 jours.
- Conformité : les politiques de rétention Teams (messages de canaux, chats) sont appliquées indépendamment de l'expiration.

## 6.8 Canaux privés

- **Autorisés avec contrôle** : créés uniquement par les propriétaires (paramètre de l'équipe).
- Chaque canal privé génère un **site SharePoint distinct** avec permissions propres → risque de gouvernance.
- Règles :
  - maximum 5 canaux privés par équipe ;
  - propriétaires du canal = propriétaires de l'équipe (≥ 2) ;
  - étiquette de sensibilité héritée ;
  - le canal privé est inclus dans l'inventaire (registre) et les Access Reviews ;
  - usage pour : contenu restreint à l'intérieur d'une équipe (RH, finance du projet). Si les besoins de confidentialité sont majeurs → créer un **site distinct**, pas un canal privé.

## 6.9 Canaux partagés

- Collaboration inter-équipes ou inter-organisations (Teams Connect) **sans changer d'équipe**.
- Canaux partagés **internes** (entre équipes du tenant) : autorisés avec approbation du propriétaire.
- Canaux partagés **externes** (Entra B2B direct connect) : **désactivés par défaut** ; autorisés uniquement pour des organisations approuvées par la sécurité, via paramètres d'accès inter-tenants (cross-tenant access settings) en liste d'autorisation.
- Chaque canal partagé a un site SharePoint associé : mêmes obligations que les canaux privés (registre, revue d'accès).
- Préférence pour l'Extranet standard (site + invités Entra) lorsqu'il y a stockage documentaire durable.

---

# 7. Gouvernance OneDrive

## 7.1 Posture restrictive

**Principe : OneDrive = espace de travail personnel et temporaire. SharePoint = lieu de collaboration et de stockage corporatif.**

### Paramètres recommandés

| Paramètre | Valeur |
|---|---|
| Partage externe OneDrive (niveau tenant) | **« Seulement les personnes de votre organisation »** (désactivé pour l'externe) |
| Liens anonymes / « Anyone » | Désactivés |
| Lien par défaut | « Personnes spécifiques » ou « Personnes de l'organisation » (interne) |
| Partage interne | Autorisé |
| Invités sur OneDrive | Aucun |
| Quota par défaut | 1 To (ajustable), alertes à 80 % |
| Synchronisation | Limitée aux appareils gérés / conformes (domaine ou Intune) |
| Rétention après départ | Le gestionnaire est propriétaire du OneDrive pour 90 jours ; transfert du contenu requis ; suppression à 93 à 180 jours selon politique |
| Dossiers connus (Known Folder Move) | Activé (protège Bureau/Documents/Images) |
| Corbeille | 93 jours |

Commande de référence :

```powershell
Set-SPOTenant -OneDriveSharingCapability Disabled   # interne uniquement
Set-SPOTenant -OneDriveLoopSharingCapability Disabled
Set-SPOTenant -OrphanedPersonalSitesRetentionPeriod 90
```

*(`Disabled` pour OneDrive = pas de partage externe ; le partage interne reste possible.)*

### Collaboration externe

Toute collaboration avec un externe → **site SharePoint Extranet** (section 3.7) ou Projet avec invités approuvés. Interdiction de partager un fichier OneDrive à l'externe, y compris par courriel (liens). Pièce jointe cloud interne uniquement ; pour l'externe, utiliser le site gouverné.

## 7.2 Justification des risques

| Risque | Détail |
|---|---|
| **Données corporatives stockées individuellement** | Le contenu d'équipe se retrouve dans des silos personnels : invisible pour l'équipe, pas de continuité, pas de gouvernance par direction |
| **Difficulté de gouvernance** | Des milliers d'espaces individuels, sans propriétaire d'équipe, sans métadonnées, sans modèle, avec des permissions ad hoc impossibles à réviser |
| **Risques lors du départ d'employés** | Perte de documents, documents partagés qui disparaissent, accès conservé par des destinataires, données exfiltrées (synchronisation, téléchargement) avant départ |
| **Partage externe non maîtrisé** | Liens envoyés vers des tiers sans validation, sans expiration, hors registre |
| **Exposition à Copilot** | Les contenus personnels partagés largement s'ajoutent aux sources accessibles à Copilot pour d'autres utilisateurs |
| **Exfiltration** | Synchronisation vers appareils non gérés ; facilité de copie |
| **Conformité** | Pas de classement officiel, rétention ou enregistrements difficiles à garantir |

## 7.3 Mesures d'accompagnement

- **Règle d'usage** : « Brouillons personnels dans OneDrive, tout contenu partagé ou officiel dans SharePoint/Teams ».
- Détection DLP/Purview : documents partagés à plus de N personnes internes ou contenu étiqueté *Confidentiel* → alerte et suggestion de déplacer vers SharePoint.
- Offboarding : processus RH/TI — 30 jours avant départ, inventaire OneDrive ; le gestionnaire reçoit l'accès ; transfert vers un site gouverné.
- **Gestion des appareils** : sync OneDrive uniquement sur appareils conformes Intune.
- Formation et page d'aide : « Où ranger mes fichiers ? ».

---

# 8. Gouvernance du partage externe SharePoint

## 8.1 Posture Zero Trust

**Ne jamais faire confiance, toujours vérifier :** chaque accès externe est nominatif, authentifié (Entra ID), approuvé, limité dans le temps, et revu.

### Paramètres tenant (SharePoint / OneDrive)

| Paramètre | Valeur |
|---|---|
| Niveau de partage externe tenant | **« Invités existants seulement »** (*Existing guests*), au maximum |
| Liens anonymes (« Anyone ») | **Désactivés** |
| Type de lien par défaut | « Personnes spécifiques » (ou interne) |
| Expiration des liens d'invité | 30 jours (non renouvelable automatiquement) |
| Invités doivent utiliser le courriel invité | **Oui** (`RequireAcceptingAccountMatchInvitedAccount = $true`) |
| Autorisation de partage par les non-propriétaires | Seuls les propriétaires de site peuvent inviter (« Only owners can share ») |
| Authentification | Entra ID B2B (code à usage unique désactivé au profit de comptes Entra/MSA/fédérés approuvés selon politique) |
| Domaines | **Liste d'autorisation** de domaines de partenaires approuvés |
| Sites Extranet | Niveau de partage de site : « Invités existants » ; autres sites : « Seulement les personnes de votre organisation », sauf approbation |
| Propriétés d'accès | Restriction de la recherche et du contenu pour invités non gérés |

Commande de référence :

```powershell
Set-SPOTenant -SharingCapability ExistingExternalUserSharingOnly
Set-SPOTenant -DefaultSharingLinkType Direct
Set-SPOTenant -RequireAcceptingAccountMatchInvitedAccount $true
Set-SPOTenant -ExternalUserExpirationRequired $true -ExternalUserExpireInDays 90
Set-SPOTenant -SharingDomainRestrictionMode AllowList -SharingAllowedDomainList "partenaire1.com partenaire2.com"
Set-SPOTenant -OnlyAllowMembersViewMembership $true
```

### Paramètres Entra ID (collaboration externe)

- **External collaboration settings** : *Guest invite restrictions* = « Seuls les utilisateurs affectés à des rôles d'administrateur spécifiques peuvent inviter » (rôle **Guest Inviter** donné aux comptes de provisionnement/TI).
- **Cross-tenant access settings** : inbound/outbound en liste d'autorisation ; confiance MFA/appareil des tenants partenaires selon évaluation.
- Entra **Entitlement Management** (Access Packages) pour les invités : catalogue « Partenaires », approbation, expiration, revues.
- Accès conditionnel dédié aux invités (MFA, conditions d'usage, appareil).
- Autorisations de consentement des applications limitées.

## 8.2 Ce qui est autorisé

- Partage **uniquement** avec :
  - des invités **déjà présents** dans Entra ID (compte B2B créé et approuvé) ;
  - des invités **approuvés par les TI** (via le processus 8.4).
- Partage par lien « Personnes spécifiques » avec ces comptes.

## 8.3 Ce qui est interdit

- Partage avec adresses courriel externes **inconnues** (invitation ad hoc).
- Invitation directe par un utilisateur sans validation TI.
- Liens anonymes ou « Anyone ».
- Liens « Personnes de l'organisation » consommés par des invités.
- Partage de dossiers/fichiers confidentiels à des externes sans étiquette adaptée.
- Partage depuis OneDrive à des externes.

Contrôles techniques : paramètres tenant ci-dessus + DLP (blocage du partage de contenu *Confidentiel/Hautement confidentiel* à l'externe) + alertes Purview sur invitation hors processus.

## 8.4 Processus d'approbation des invités

```
Demande d'invité (portail) → Approbation gestionnaire / propriétaire
→ Validation TI (identité, organisation, domaine) → [Validation Sécurité si Extranet / confidentiel]
→ Création du compte B2B (Graph /invitations ou Access Package)
→ Ajout au groupe du site → Conditions d'utilisation (ToU) acceptées
→ Notification → Inscription au registre des invités
```

Informations requises : nom, courriel professionnel (pas de courriel personnel gratuit sauf dérogation), organisation, justification, espace(s) visé(s), durée, parrain interne (**sponsor**), niveau d'accès.

Critères de validation TI : domaine de l'entreprise partenaire dans la liste d'autorisation ou entente existante ; identité confirmée (contact du sponsor) ; principe du moindre privilège.

## 8.5 Cycle de vie des invités

| Étape | Règle |
|---|---|
| **Création** | Via portail/Access Package, sponsor interne obligatoire, attribut `CompanyName` + `extensionAttribute` (projet, date de fin) |
| **Utilisation** | Accès uniquement aux espaces approuvés ; MFA obligatoire ; ToU acceptées |
| **Revue** | Trimestrielle (Extranet/confidentiel), semestrielle (autres) via Access Reviews, par le sponsor/propriétaire |
| **Expiration** | Automatique : 90 jours par défaut, renouvelable sur revue (max 12 mois) ; fin immédiate à la clôture du projet |
| **Inactivité** | Aucune connexion depuis 60 jours → désactivation ; 90 jours → suppression |
| **Suppression** | Compte B2B supprimé (et retrait des accès) ; journalisation ; liens supprimés |

## 8.6 Revue périodique des accès invités

- **Access Reviews** (Entra ID Governance) ciblant les invités par Groupe et par application.
- Rapports : invités sans sponsor, invités inactifs, invités avec accès à plusieurs espaces.
- Si la revue n'est pas complétée dans les 14 jours : **retrait automatique** (*Auto apply results*, valeur par défaut « Deny »).
- Résultats consignés pour audit (Purview).

## 8.7 Expiration automatique

- Expiration des liens d'invité (SharePoint) : 30 jours.
- Expiration de l'appartenance aux Groupes/Packages d'accès : 90 jours renouvelables.
- Expiration du Groupe M365 (365 jours).
- Les sites Extranet sont liés à la date de fin de l'entente ; à l'échéance, tous les invités sont retirés et le site passe en lecture seule.

---

# 9. Sécurité Microsoft 365

## 9.1 Recommandations clés

### MFA obligatoire
- MFA pour **tous** les utilisateurs (internes, invités, administrateurs), via accès conditionnel (pas de « Security defaults » seuls).
- Méthodes résistantes à l'hameçonnage pour administrateurs et rôles sensibles : **FIDO2 / Windows Hello / Passkeys**, Authenticator avec correspondance de nombre. Désactivation des méthodes SMS/voix à terme.
- Rôles admin protégés par **PIM** (just-in-time, approbation, justification).

### Accès conditionnel
- Bloquer l'authentification héritée (legacy).
- Exiger MFA pour tous les accès cloud, MFA renforcée pour admins.
- Exiger appareil conforme/joint hybride pour accéder à SharePoint/Teams/OneDrive avec données sensibles ; sinon **accès web limité** (pas de téléchargement, impression, synchronisation) via contrôles de session (*Conditional Access App Control* / SharePoint « Allow limited, web-only access »).
- Politique dédiée **invités** : MFA, ToU, session limitée, aucun accès hors applications ciblées.
- Risque utilisateur/connexion (Entra ID Protection) : blocage ou réinitialisation du mot de passe en risque élevé.
- **Authentication context** pour exiger une réauthentification sur les sites étiquetés *Hautement confidentiel*.
- Restrictions de localisation (pays autorisés).

### Sensitivity Labels
- Taxonomie simple (4 niveaux) : **Général**, **Interne**, **Confidentiel**, **Hautement confidentiel** (+ sous-étiquette *Confidentiel – Externe* pour Extranet).
- Étiquettes de **conteneur** (Groupes/Teams/Sites) : confidentialité, partage externe, accès non géré, contexte d'authentification.
- Étiquettes de **fichier** : chiffrement, marquage, droits (Azure RIP/ MIP).
- **Étiquetage automatique** (service-side et client) sur types d'informations sensibles.
- Étiquette par défaut sur bibliothèques SharePoint ; obligation d'étiquette dans Office.

### Microsoft Purview
- **Information Protection** (étiquettes), **Data Loss Prevention**, **Data Lifecycle Management** (rétention), **Records Management**, **Insider Risk Management**, **Communication Compliance**, **eDiscovery**, **Audit**, **Data Security Posture Management (DSPM) pour l'IA**.
- Tableau de bord Compliance Manager pour mesurer l'alignement réglementaire.

### DLP
- Politiques sur Exchange, SharePoint, OneDrive, Teams (chat/canaux) et appareils (Endpoint DLP).
- Règles : bloquer le partage externe de contenu contenant renseignements personnels, financiers ou étiquetés *Confidentiel+* ; alerter sur le téléversement vers des services non autorisés ; avertissement avec justification (*policy tips*).
- Mode simulation 30 jours avant application.
- **DLP pour Copilot** : exclusion de contenu étiqueté de certaines réponses/résumés (emplacement *Microsoft 365 Copilot*).

### Audit
- **Audit (Standard/Premium)** activé, conservation 1 an (10 ans en Premium selon besoin).
- Événements clés : création/suppression de sites, changements de permissions, partage externe, invitations d'invités, accès à des fichiers sensibles, activités admin.
- Envoi vers Microsoft Sentinel (SIEM) pour corrélation et alertes.
- Politiques d'alerte : invitation d'invité hors processus, partage anonyme tenté, téléchargement massif, élévation de privilèges.

### Access Reviews
- Groupes M365/Teams, applications, rôles privilégiés (PIM), invités (voir 5.3 et 8.6).
- Revues planifiées, décision automatique en cas de non-réponse, preuves archivées.

### Gestion des appareils
- **Intune** : conformité (chiffrement, antivirus, version OS), MAM/APP pour appareils personnels (BYOD) sans inscription complète.
- Appareils non gérés : web seulement, sans téléchargement.
- Defender for Endpoint : signaux de risque injectés dans l'accès conditionnel.
- OneDrive Sync limité aux appareils joints/conformes.

## 9.2 Protection de SharePoint

- Étiquettes de site obligatoires + partage externe limité par étiquette.
- Désactivation des liens anonymes ; liens « personnes spécifiques » par défaut.
- **SharePoint Advanced Management** : rapports de surpartage, restriction d'accès aux sites (*Restricted Access Control*), revues d'accès au site, politiques d'inactivité, *Data Access Governance* (DAG).
- Contrôle du « Everyone except external users » : désactivé/surveillé.
- Restriction de la création de permissions uniques (alerte au-delà d'un seuil).
- Audit des changements de permissions.
- Bloquer le téléchargement sur appareils non gérés.
- Sauvegarde/restauration : **Microsoft 365 Backup** ou solution tierce pour les sites critiques ; corbeille 93 jours ; restauration de site/bibliothèque (rançongiciel).

## 9.3 Protection de Teams

- Étiquettes de conteneur (confidentialité, invités, accès non géré).
- Stratégies de réunion : salle d'attente pour non-membres, présentateurs limités, pas d'enregistrement par défaut pour invités, filigrane/chiffrement de bout en bout pour réunions sensibles (Teams Premium).
- Stratégies de messagerie, d'applications, de canaux.
- DLP Teams (chat/canal) ; Communication Compliance si requis.
- Rétention des messages (3 ans) et eDiscovery.
- Paramètres de partage fédéré (domaines externes Teams) en liste d'autorisation.
- Protection contre les liens/fichiers malveillants (Defender for Office 365 — *Safe Links/Safe Attachments* pour Teams).

## 9.4 Protection de OneDrive

- Partage externe désactivé (section 7).
- Étiquetage par défaut ; DLP sur contenus sensibles.
- Synchronisation limitée aux appareils gérés ; *Known Folder Move*.
- Accès limité sur appareils non gérés.
- Politique de rétention/départ des employés ; transfert au gestionnaire.
- Restauration de OneDrive (rançongiciel) : 30 jours.
- Détection d'activités anormales (téléchargements massifs, suppressions massives) avec Defender for Cloud Apps/Insider Risk.

---

# 10. Gouvernance Copilot

## 10.1 Copilot hérite des permissions existantes

- Microsoft 365 Copilot interroge Microsoft Graph et **ne retourne que le contenu auquel l'utilisateur a déjà accès** (SharePoint, OneDrive, Teams, Exchange…).
- Il **n'ajoute aucun droit**, mais il **révèle** ce qui était accessible mais ignoré (« sécurité par obscurité »).
- Conséquence : *chaque erreur de permission devient une fuite potentielle à la vitesse de la conversation*.
- Il respecte les étiquettes de sensibilité (droits d'utilisation, chiffrement) et hérite de l'étiquette la plus restrictive des sources dans les réponses.

## 10.2 Importance du nettoyage des accès

Avant le déploiement général de Copilot :

1. **Inventaire** : tous les sites, Groupes, Teams, propriétaires, invités (registre + rapports SAM).
2. **Rapports de surpartage** (SAM *Data Access Governance*) : sites avec « Everyone except external users », liens « Organisation entière », permissions uniques nombreuses, sites accessibles à de très grands groupes.
3. **Remédiation** : suppression des accès excessifs, remplacement des groupes larges par des groupes de sécurité ciblés, correction des liens.
4. **Revues d'accès** par les propriétaires.
5. **Nettoyage du contenu ROT** : archiver/supprimer obsolète et dupliqué (améliore la qualité des réponses).
6. Ré-évaluation périodique (trimestrielle).

## 10.3 Contrôle du surpartage

- Liens « Anyone » et « Organisation » désactivés ou restreints ; lien par défaut « Personnes spécifiques ».
- **Restricted Access Control (RAC)** pour restreindre un site à un groupe de sécurité (même si des liens existent).
- **Restricted SharePoint Search** (mesure temporaire de déploiement) : limiter Copilot/Recherche organisationnelle à une liste de sites validés pendant le nettoyage — à utiliser comme *filet transitoire*, pas comme solution durable.
- Rapports « Site access review » et « Permissions report » pour les propriétaires.
- Seuil d'alerte sur permissions uniques / partages massifs.

## 10.4 Gestion des données sensibles

- **Étiquettes de sensibilité** appliquées aux sites et fichiers ; **chiffrement** avec droits d'utilisation (Copilot ne peut pas extraire si l'utilisateur n'a pas le droit EXTRACT/VIEW).
- **Étiquetage automatique** des documents sensibles existants (RH, finance, juridique, renseignements personnels).
- **DLP pour Microsoft 365 Copilot** : exclusion du traitement des fichiers/courriels selon l'étiquette ou le type d'information sensible.
- **DSPM pour l'IA** (Purview) : visibilité sur les interactions Copilot, détection d'invites et de réponses à risque, recommandations (« risk assessments » de surpartage).
- **Insider Risk / Communication Compliance** : détection d'usage risqué de l'IA.
- Audit et conservation des interactions Copilot (rétention Purview), eDiscovery.

## 10.5 Restricted Content Discovery (RCD)

- Fonction de SharePoint Advanced Management : **retire un site de la découverte par Copilot et de la recherche organisationnelle**, sans modifier les permissions.
- Usage : sites sensibles à permissions encore imparfaites (RH, juridique, direction, M&A), pendant ou après le nettoyage.
- Prise en charge par site (`Set-SPOSite -RestrictContentOrgWideSearch $true`).
- Attention : RCD ne remplace pas les permissions ; les utilisateurs ayant déjà accès peuvent encore ouvrir le contenu directement, et Copilot peut l'utiliser si l'utilisateur le fournit explicitement dans une demande (selon le comportement actuel du produit — à valider à chaque évolution).

## 10.6 SharePoint Advanced Management (SAM)

Inclus avec les licences Copilot ; capacités à activer :

| Capacité SAM | Usage |
|---|---|
| **Data Access Governance (DAG)** | Rapports de surpartage, sites à fort partage, *Everyone* |
| **Site Access Reviews** | Revue par les propriétaires pour les sites sur-exposés |
| **Restricted Access Control** | Restriction d'accès site par site |
| **Restricted Content Discovery** | Exclusion de la découverte Copilot |
| **Inactive Sites Policy** | Détection/archivage des sites inactifs |
| **Site Ownership Policy** | Gestion des sites sans propriétaire |
| **Site Lifecycle Management** | Politiques de cycle de vie |
| **Conditional Access for sites** | Contexte d'authentification par site |
| **Change history / Recent actions** | Traçabilité des changements |
| **Block download policy** | Pas de téléchargement sur appareils non gérés |
| **Microsoft 365 Archive** | Archivage à coût réduit |

## 10.7 Purview pour Copilot

- Étiquettes de sensibilité, DLP, rétention, audit, eDiscovery, Communication Compliance, Insider Risk.
- **DSPM pour l'IA** : tableau de bord d'activités IA, évaluations de données (*data assessments*) pour détecter les sites à risque, politiques en un clic.
- **Politiques de rétention** pour les interactions Copilot (invites/réponses).
- Alertes sur divulgation d'informations sensibles dans les invites.

## 10.8 Gouvernance d'usage de Copilot

- Déploiement **par vagues** (pilote → direction → généralisation), conditionné aux critères de préparation (section 13, phase 6).
- Licences attribuées via un groupe Entra (*license assignment*) ; formation obligatoire.
- Politique d'utilisation acceptable (vérification des réponses, pas de décision automatisée sans humain, citations, confidentialité).
- Agents et plugins : catalogue approuvé, **Copilot Control System** (centre d'admin), restriction de la création d'agents (Copilot Studio) à un groupe encadré, DLP Power Platform.
- Mesure d'adoption et de risque (rapports d'usage, DSPM).

---

# 11. Cycle de vie

Modèle unique : **Création → Utilisation → Revue → Archivage → Suppression**

## 11.1 Sites SharePoint

| Phase | Règles |
|---|---|
| **Création** | Demande portail, approbations, gabarit, ≥ 2 propriétaires, étiquette, rétention, registre |
| **Utilisation** | Permissions par groupes, métadonnées, pas de partage non autorisé, surveillance SAM |
| **Revue** | Annuelle (Équipe/Communication/Communauté), semestrielle (Projet), trimestrielle (Extranet) : accès, propriétaires, pertinence, classification |
| **Archivage** | Inactif 12 mois ou fin de projet : avis 30 j → lecture seule → archivage (M365 Archive), exclusion de la recherche |
| **Suppression** | Après la période de rétention et absence de gel : suppression (corbeille 93 j) ; journalisation ; mise à jour du registre |

## 11.2 Teams

| Phase | Règles |
|---|---|
| **Création** | Portail, modèle approuvé, ≥ 2 propriétaires, étiquette, canaux standards |
| **Utilisation** | Canaux privés/partagés encadrés, applications approuvées, invités approuvés |
| **Revue** | Annuelle (permanente), semestrielle (projet) ; renouvellement de l'expiration du Groupe |
| **Archivage** | Inactif 6 mois ou fin de projet : archivage Teams (lecture seule) |
| **Suppression** | Expiration du Groupe + rétention : suppression du Team, du site et des ressources liées ; restauration 30 jours |

## 11.3 Groupes Microsoft 365

| Phase | Règles |
|---|---|
| **Création** | Uniquement via le portail/Graph, nommage conforme, propriétaires ≥ 2, étiquette de conteneur |
| **Utilisation** | Appartenance gérée par propriétaires ; pas de groupes dynamiques pour les sites sensibles sans validation |
| **Revue** | **Politique d'expiration** (365 j, renouvellement par propriétaire ou activité) ; Access Reviews annuelles |
| **Archivage** | Associé à l'archivage du Team/site ; Groupe masqué de la liste d'adresses global |
| **Suppression** | Suppression logique 30 jours, restauration possible ; suppression définitive après rétention |

## 11.4 Invités

| Phase | Règles |
|---|---|
| **Création** | Demande portail/Access Package, sponsor, validation TI (+ sécurité si requis), ToU, MFA |
| **Utilisation** | Accès minimal, accès conditionnel invités, aucune élévation de droits |
| **Revue** | Trimestrielle (Extranet/confidentiel), semestrielle (autres), par le sponsor |
| **Archivage** | Désactivation à 60 j d'inactivité ou fin de projet/entente (conserver trace d'audit) |
| **Suppression** | Suppression du compte à 90 j d'inactivité ou à la fin d'entente ; retrait de tous les accès |

## 11.5 Déclencheurs automatisés

- Registre central des espaces (Dataverse/ServiceNow CMDB) avec états : *Demandé, Actif, En revue, Lecture seule, Archivé, Supprimé*.
- Flux planifiés (Power Automate / Azure Automation / Logic Apps) pour les rappels et transitions.
- Tableau de bord Power BI du cycle de vie.

---

# 12. Matrice RACI

**Légende :** **R** = Responsable (exécute) · **A** = Approbateur (décide / redevable) · **C** = Consulté · **I** = Informé

| Activité | TI (M365) | Sécurité | Gestionnaires | Propriétaires de sites | Utilisateurs |
|---|:-:|:-:|:-:|:-:|:-:|
| Définir la politique de gouvernance | R | C | C | I | I |
| Approuver la politique de gouvernance (comité) | C | A | A | I | I |
| Soumettre une demande d'espace | I | I | C | R | R (demandeur) |
| Approuver la pertinence métier de la demande | I | I | **A** | C | I |
| Valider la conformité au catalogue (TI) | **R/A** | C | I | I | I |
| Valider la sécurité (Extranet, confidentiel, externes) | C | **R/A** | I | C | I |
| Créer l'espace (provisioning Graph) | **R** | I | I | I | I |
| Maintenir les gabarits | **R/A** | C | C | C | I |
| Désigner et maintenir ≥ 2 propriétaires | C | I | **A** | **R** | I |
| Gérer les membres et les accès quotidiens | I | I | I | **R/A** | I |
| Approuver un invité externe | R (validation) | **A** (si requis) | C | C (sponsor) | I |
| Revue des accès (annuelle / trimestrielle) | C (outil) | C | **A** | **R** | I |
| Classification et étiquetage des contenus | C | A (taxonomie) | I | **R** | **R** |
| Configuration Purview (DLP, étiquettes, rétention) | R | **A** | C | I | I |
| Configuration Entra (MFA, accès conditionnel) | R | **A** | I | I | I |
| Gestion des sites orphelins / inactifs | **R** | I | A (réaffectation) | R | I |
| Archivage et suppression | **R** | C | A | C | I |
| Surveillance, audit, incidents | R | **A** | I | C | I |
| Préparation et gouvernance de Copilot | R | **A (risques)** | C | R (nettoyage des sites) | I |
| Formation et communication | **R** | C | C | C | I |
| Respect des règles d'usage (OneDrive/SharePoint) | I | I | C | R | **R** |

> **Notes :** (1) Un seul « A » par activité idéalement ; les cas à double « A » (politique, approbation conjointe) sont assumés par le comité de gouvernance M365 (TI + Sécurité + représentants des directions). (2) Les **Gestionnaires** sont les responsables hiérarchiques/direction ; les **Propriétaires de sites** sont les responsables opérationnels de l'espace.

### Comité de gouvernance M365
- Composition : architecte M365 (président), responsable sécurité, responsable gestion documentaire/conformité, représentants des directions, représentant RH/juridique.
- Fréquence : mensuelle (déploiement), trimestrielle (régime permanent).
- Rôles : arbitrer les dérogations, valider les gabarits, suivre les KPIs.

---

# 13. Feuille de route de mise en œuvre

Durée indicative totale : **9 à 12 mois**, avec chevauchements possibles.

## Phase 1 — Bloquer les créations libres (Semaines 1-4)

**Objectif :** arrêter la prolifération.

- Inventaire initial (sites, Groupes, Teams, propriétaires, invités, partage).
- Communication aux directions et aux utilisateurs (pourquoi, quand, comment).
- Restreindre la création de Groupes M365 (`GroupCreationAllowedGroupId`).
- Désactiver la création de sites par les utilisateurs (SharePoint).
- Mettre en place un **processus provisoire** (formulaire simple + boîte de service) pour ne pas bloquer les métiers.
- Revue des rôles d'administrateur (PIM).

**Livrables :** inventaire, paramètres appliqués, FAQ, processus transitoire.
**Critère de sortie :** 0 création libre observée dans l'audit pendant 2 semaines.

## Phase 2 — Mettre en place le portail de demande (Semaines 4-12)

- Choix Power Apps ou ServiceNow (décision d'architecture).
- Conception du formulaire, du registre (Dataverse/CMDB), des flux d'approbation.
- Développement du provisioning Graph (App Registration, `Sites.Selected`, journalisation).
- Convention de nommage, politique de nommage Entra.
- Tests (tenant de développement) et pilote avec 2-3 directions.
- Formation des approbateurs et propriétaires.

**Livrables :** portail en production, runbooks, registre des espaces, tableaux de bord.
**Critère de sortie :** délai moyen de provisioning ≤ 2 jours ouvrables ; 100 % des demandes via le portail.

## Phase 3 — Déployer les gabarits (Semaines 8-16)

- Concevoir et publier les 5 gabarits (PnP/Site Designs) avec Hubs, types de contenu, métadonnées, navigation, branding.
- Modèles Teams approuvés.
- Taxonomie (Term Store) et hub de types de contenu.
- Création des Hubs par direction.
- Gouvernance des propriétaires (≥ 2), contrôles mensuels, sites orphelins.
- **Remédiation du parc existant** : rattachement aux Hubs, affectation de propriétaires, regroupement/archivage des doublons.

**Livrables :** catalogue de gabarits versionné, Hubs, processus orphelins.
**Critère de sortie :** 100 % des nouveaux espaces issus de gabarits ; ≥ 90 % des sites existants avec 2 propriétaires.

## Phase 4 — Sécuriser le partage externe (Semaines 12-22)

- Passer le tenant en « Invités existants seulement », désactiver Anyone.
- OneDrive : partage interne seulement.
- Entra : restriction des invitations, Entitlement Management, ToU, expiration, accès conditionnel invités, cross-tenant settings.
- Processus d'approbation des invités et registre.
- **Assainissement** : recensement des liens anonymes/externes existants, migration vers des Extranets, révocation des liens non justifiés.
- Access Reviews des invités.

**Livrables :** politique de partage externe appliquée, processus invités, tableau de bord.
**Critère de sortie :** 0 lien anonyme ; 100 % des invités avec sponsor et date d'expiration.

## Phase 5 — Déployer Purview (Semaines 16-32)

- Taxonomie d'étiquettes de sensibilité (conteneur + fichier), publication par vagues.
- Politiques DLP (mode simulation puis application).
- Rétention et enregistrements (avec gestion documentaire/juridique).
- Audit, alertes, intégration Sentinel.
- Étiquetage automatique, Insider Risk (selon licences).
- Access Reviews récurrentes.
- Formation à la classification.

**Livrables :** étiquettes et DLP actifs, politiques de rétention, tableaux de conformité.
**Critère de sortie :** ≥ 90 % des sites étiquetés ; DLP en mode application sur les cas critiques.

## Phase 6 — Préparation de Copilot (Semaines 24-40)

- SAM : DAG (rapports de surpartage), RAC, RCD, politique d'inactivité, Archive.
- Nettoyage des accès et du contenu ROT ; revues par les propriétaires.
- Restricted SharePoint Search (transitoire) si nécessaire pour le pilote.
- DSPM pour l'IA, DLP pour Copilot, rétention des interactions.
- Politique d'utilisation acceptable, formation, champions.
- **Pilote Copilot** (100-300 utilisateurs) → mesure → déploiement par vagues.
- Gouvernance des agents/plugins (Copilot Control System).

**Livrables :** rapport de préparation Copilot, plan de déploiement, KPIs d'adoption et de risque.
**Critère de sortie :** 100 % des sites sensibles remédiés ou protégés (RCD/RAC) ; surpartage sous le seuil cible ; feu vert du comité.

## Vue calendrier

```
Mois      1   2   3   4   5   6   7   8   9   10
Phase 1   ███
Phase 2       ██████
Phase 3           ██████
Phase 4               ████████
Phase 5                   ██████████
Phase 6                       ██████████
Opération continue (revues, KPIs, amélioration)  ──────────────►
```

## Facteurs de réussite

- Sponsor exécutif et comité de gouvernance actifs.
- Portail **simple et rapide** (sinon, le shadow IT revient).
- Communication, formation, champions dans les directions.
- Gestion du changement : expliquer le « pourquoi », publier les SLA.
- Mesure et transparence (tableau de bord public des KPIs).
- Gouvernance « comme du code » (gabarits versionnés, pipelines).

---

# 14. Décisions de gouvernance recommandées

| # | Décision | Justification |
|---|---|---|
| D1 | Interdire la création libre de Groupes M365, sites et Teams ; tout passe par le portail | Source de la prolifération et du surpartage |
| D2 | Catalogue limité à 5 types d'espaces ; dérogation par comité | Standardisation et gouvernabilité |
| D3 | Gabarits obligatoires pour tout provisioning | Sécurité et conformité dès la création |
| D4 | Minimum 2 propriétaires par site/Team, contrôle mensuel | Éviter les orphelins |
| D5 | Date de fin obligatoire pour les projets et Extranets | Cycle de vie maîtrisé |
| D6 | Architecture plate avec Hubs, sans sous-sites | Simplicité, sécurité, recherche |
| D7 | OneDrive : aucun partage externe | Réduire l'exposition des données individuelles |
| D8 | Zero Trust pour l'externe : invités Entra existants et approuvés TI seulement, pas de liens anonymes | Contrôle de l'identité et traçabilité |
| D9 | Expiration automatique des invités (90 jours) et revues trimestrielles pour Extranet | Moindre privilège dans le temps |
| D10 | MFA obligatoire + accès conditionnel + appareils conformes pour données sensibles | Protection des identités |
| D11 | Étiquettes de sensibilité obligatoires sur les conteneurs et fichiers | Base de la DLP, du chiffrement et de Copilot |
| D12 | Archivage/suppression automatisés des sites inactifs (12 mois) et des Teams inactifs (6 mois) | Réduction du bruit et de la surface d'attaque |
| D13 | Aucun déploiement large de Copilot avant nettoyage des accès et validation des critères | Éviter l'exposition de données par surpartage |
| D14 | Utilisation de SAM (DAG, RAC, RCD) comme prérequis de Copilot | Visibilité et correction du surpartage |
| D15 | Registre central unique des espaces comme source de vérité du cycle de vie | Traçabilité, audit, automatisation |
| D16 | Comité de gouvernance M365 pour arbitrer les dérogations | Décisions cohérentes et documentées |
| D17 | Canaux privés/partagés encadrés (limite, propriétaires, registre) ; canaux partagés externes désactivés par défaut | Maîtriser les sites cachés |
| D18 | Provisioning par identité applicative au moindre privilège (pas de compte humain) | Sécurité du processus lui-même |

---

# 15. Risques atténués

| Risque initial | Mesure | Risque résiduel |
|---|---|---|
| Prolifération d'espaces | Création bloquée, portail, catalogue limité | Faible (dérogations suivies) |
| Sites/Teams orphelins | ≥ 2 propriétaires, contrôles mensuels, expiration des Groupes | Faible |
| Fuite via partage externe | Zero Trust, invités approuvés, pas d'Anyone, DLP | Faible à moyen (erreur humaine, invité compromis) |
| Fuite via OneDrive | Partage externe désactivé, DLP, appareils gérés | Faible |
| Surpartage exposé par Copilot | Nettoyage, SAM (DAG/RAC/RCD), étiquettes, DLP Copilot | Moyen → faible après phase 6 |
| Compromission de comptes | MFA, accès conditionnel, PIM, Identity Protection | Faible à moyen |
| Non-conformité (rétention/litiges) | Gabarits avec rétention, étiquettes, audit, eDiscovery | Faible |
| Départ d'employés / perte de données | Propriétaires multiples, transfert OneDrive, offboarding | Faible |
| Recherche inefficace / contenu obsolète | Métadonnées, Hubs, archivage, suppression, ROT | Faible à moyen |
| Shadow IT (portail lent) | Portail simple, SLA, communication | Moyen (à surveiller) |
| Dérive de configuration | Gouvernance as code, rapports SAM, audit | Faible |
| Compte de provisioning compromis | Identité applicative moindre privilège, certificats, rotation, alertes | Faible |
| Coûts de stockage | Versionnage limité, archivage, suppression | Faible |

---

# 16. Bénéfices attendus

**Sécurité**
- Réduction de la surface d'exposition (moins d'espaces, accès maîtrisés, externe contrôlé).
- Traçabilité complète des créations, invitations et partages.

**Conformité**
- Rétention et classification appliquées dès la création.
- Preuves d'audit (revues d'accès, approbations, registre).

**Efficacité opérationnelle**
- Provisioning automatisé en heures plutôt qu'en jours de travail manuel.
- Moins de tickets de support, de restaurations et de nettoyage.
- Moins de coûts de stockage.

**Expérience utilisateur et adoption**
- Espaces prêts à l'emploi, structure familière, recherche plus pertinente.
- Un point d'entrée unique et clair.

**Qualité de l'information**
- Métadonnées cohérentes, contenu à jour, moins de doublons.

**Copilot**
- Réponses plus pertinentes et plus sûres (contenu propre, permissions saines).
- Déploiement accéléré grâce à une base déjà gouvernée.
- Réduction du risque de divulgation involontaire.

**Gouvernance**
- Rôles clairs (RACI), décisions documentées, amélioration continue.

---

# 17. KPIs de suivi

## 17.1 Provisioning et prolifération

| KPI | Cible | Fréquence |
|---|---|---|
| % des espaces créés via le portail | 100 % | Mensuelle |
| Délai moyen de provisioning (demande → disponible) | ≤ 2 jours ouvrables | Mensuelle |
| Délai de traitement par étape d'approbation | ≤ 2 jours | Mensuelle |
| Taux de refus / retour pour non-conformité | < 15 % (indicateur de clarté du formulaire) | Mensuelle |
| Nombre de dérogations accordées | Tendance décroissante | Trimestrielle |
| Nombre total de sites / Teams / Groupes (croissance nette) | Croissance maîtrisée | Mensuelle |
| Satisfaction des demandeurs (CSAT) | ≥ 4/5 | Trimestrielle |

## 17.2 Qualité de gouvernance

| KPI | Cible |
|---|---|
| % des sites avec ≥ 2 propriétaires actifs | ≥ 98 % |
| Nombre de sites orphelins | 0 (délai de correction ≤ 14 j) |
| % des sites associés à un Hub | ≥ 95 % |
| % des sites créés par gabarit | 100 % |
| % des sites avec métadonnées complètes | ≥ 90 % |
| % des sites inactifs > 12 mois traités | ≥ 95 % |
| % des Teams inactifs > 6 mois archivés | ≥ 95 % |
| Taux de conformité au nommage | ≥ 98 % |
| Revues d'accès complétées dans les délais | ≥ 95 % |

## 17.3 Sécurité et partage

| KPI | Cible |
|---|---|
| Liens anonymes / « Anyone » actifs | 0 |
| Partages externes hors processus | 0 (alerte immédiate) |
| % des invités avec sponsor et date d'expiration | 100 % |
| Invités inactifs > 90 jours | 0 |
| Délai de traitement d'une demande d'invité | ≤ 2 jours |
| % des utilisateurs avec MFA | 100 % |
| % des administrateurs avec PIM et MFA résistante à l'hameçonnage | 100 % |
| Connexions bloquées par accès conditionnel (tendance) | Suivi |
| Incidents de fuite de données liés au partage | 0 |
| % des appareils conformes accédant aux données sensibles | ≥ 95 % |

## 17.4 Protection de l'information

| KPI | Cible |
|---|---|
| % des sites étiquetés | ≥ 95 % |
| % des fichiers sensibles étiquetés (auto + manuel) | ≥ 80 % (puis progression) |
| Correspondances DLP : bloquées / contournées avec justification | Suivi, tendance à la baisse |
| Faux positifs DLP | < 10 % |
| % du contenu couvert par une politique de rétention | ≥ 95 % |

## 17.5 Copilot

| KPI | Cible |
|---|---|
| Nombre de sites avec surpartage critique (DAG) | 0 avant déploiement général |
| Sites sensibles protégés (RAC/RCD/étiquette) | 100 % |
| Permissions « Everyone except external users » sur sites sensibles | 0 |
| Taux d'adoption Copilot (utilisateurs actifs / licenciés) | ≥ 70 % |
| Incidents d'exposition de données via Copilot | 0 |
| Interactions Copilot signalées par DSPM pour l'IA | Suivi, tendance à la baisse |
| Satisfaction et gains de productivité | Suivi trimestriel |

---

# 18. Indicateurs de conformité

| Indicateur | Source | Seuil de conformité | Fréquence |
|---|---|---|---|
| Registre des espaces à jour (100 % des sites/Teams/Groupes présents) | Registre vs. Graph/SPO | 100 % | Mensuelle |
| Espaces avec étiquette de sensibilité | Purview / Graph | ≥ 95 % | Mensuelle |
| Espaces avec politique de rétention applicable | Purview | ≥ 95 % | Trimestrielle |
| Revues d'accès complétées (preuves archivées) | Entra Access Reviews | ≥ 95 % | Selon cycle |
| Approbations tracées (gestionnaire/TI/sécurité) pour 100 % des créations | Portail | 100 % | Mensuelle |
| Invités avec ToU acceptées, MFA, sponsor, expiration | Entra ID | 100 % | Mensuelle |
| Liens anonymes / Anyone | SharePoint Admin / SAM | 0 | Hebdomadaire |
| Partage externe OneDrive | SharePoint Admin | 0 | Hebdomadaire |
| Violations DLP non traitées > 5 jours | Purview | 0 | Hebdomadaire |
| Événements d'audit conservés selon la politique (≥ 1 an) | Purview Audit | 100 % | Trimestrielle |
| Actions de privilège élevé sous PIM | Entra PIM | 100 % | Mensuelle |
| Conformité MFA | Entra | 100 % | Hebdomadaire |
| Conformité des appareils | Intune | ≥ 95 % | Hebdomadaire |
| Gels légaux respectés (aucune suppression d'un contenu sous gel) | Purview eDiscovery | 100 % | Continue |
| Score Compliance Manager (cadre applicable : loi sur la protection des renseignements personnels, ISO 27001, etc.) | Purview Compliance Manager | Amélioration continue / cible fixée | Trimestrielle |
| Cycle de vie respecté (archivage/suppression dans les délais) | Registre | ≥ 95 % | Mensuelle |
| Préparation Copilot (critères de la phase 6 atteints) | Rapport SAM/DSPM | 100 % avant généralisation | Par vague |

**Gouvernance des indicateurs :** tableau de bord Power BI alimenté par Graph, SharePoint Admin, Purview et le registre ; revue mensuelle par le comité de gouvernance ; rapport trimestriel à la direction ; écarts > seuil → plan d'action avec échéance et responsable.

---

# 19. Annexes

## Annexe A — Commandes de référence (à valider selon la version des modules)

```powershell
# Création de groupes M365 : restreindre à un groupe
Connect-MgGraph -Scopes "Directory.ReadWrite.All","Group.ReadWrite.All"
$template = Get-MgBetaDirectorySettingTemplate | ? DisplayName -eq "Group.Unified"
$setting  = New-MgBetaDirectorySetting -TemplateId $template.Id -Values @(
  @{ Name="EnableGroupCreation"; Value="false" },
  @{ Name="GroupCreationAllowedGroupId"; Value="<ObjectId SG-M365-GroupCreators>" },
  @{ Name="UsageGuidelinesUrl"; Value="https://intranet/portail-m365-aide" }
)

# SharePoint : création de sites par les utilisateurs désactivée
Connect-SPOService -Url https://<tenant>-admin.sharepoint.com
Set-SPOTenant -SelfServiceSiteCreationDisabled $true
Set-SPOTenant -DisableSubsiteCreation $true   # selon disponibilité

# Partage externe
Set-SPOTenant -SharingCapability ExistingExternalUserSharingOnly
Set-SPOTenant -OneDriveSharingCapability Disabled
Set-SPOTenant -DefaultSharingLinkType Direct
Set-SPOTenant -RequireAcceptingAccountMatchInvitedAccount $true
Set-SPOTenant -ExternalUserExpirationRequired $true -ExternalUserExpireInDays 90

# Restricted Content Discovery (site)
Set-SPOSite -Identity https://<tenant>.sharepoint.com/sites/<site> -RestrictContentOrgWideSearch $true
```

## Annexe B — Permissions applicatives Graph du provisioning (moindre privilège)

| Permission | Usage |
|---|---|
| `Group.Create` | Création des Groupes M365 |
| `Team.Create`, `TeamSettings.ReadWrite.All` | Création/paramétrage des Teams |
| `Sites.Selected` (+ attribution par site) | Application des gabarits sans accès global |
| `User.Read.All` | Validation des propriétaires |
| `User.Invite.All` | Création d'invités B2B (processus approuvé) |
| `GroupMember.ReadWrite.All` (ou ciblé) | Gestion des propriétaires/membres |
| `Directory.Read.All` | Lecture des paramètres/nommage |
| `InformationProtectionPolicy.Read.All` | Lecture des étiquettes |

Mesures : certificat/Managed Identity (pas de secret), rotation, restriction réseau, journalisation, alertes sur usage anormal, revue trimestrielle des permissions.

## Annexe C — Hypothèses et points à valider

- Licences : Microsoft 365 E3/E5 (ou équivalent), **Entra ID P2 / Governance** (Access Reviews, Entitlement Management, PIM), **Purview** (niveau E5 pour étiquetage automatique, DLP avancé, Insider Risk), **SharePoint Advanced Management** (inclus avec Copilot), **Teams Premium** (optionnel), **Microsoft 365 Copilot**.
- Durées de rétention indicatives : à valider avec la gestion documentaire et le juridique.
- Seuils d'inactivité (12 mois sites, 6 mois Teams), délais d'expiration (90 jours invités) : à ajuster selon le contexte organisationnel et réglementaire.
- Le portail (Power Apps vs ServiceNow) dépend de l'écosystème existant.
- Les fonctionnalités Microsoft (SAM, RCD, DSPM pour l'IA, Copilot Control System, M365 Archive) évoluent rapidement : **valider la disponibilité, les noms et les licences dans la documentation Microsoft à jour avant implémentation**.
- Les commandes et paramètres sont fournis à titre de référence ; les tester dans un tenant de développement.

## Annexe D — Glossaire

| Terme | Définition |
|---|---|
| **SAM** | SharePoint Advanced Management |
| **RAC** | Restricted Access Control |
| **RCD** | Restricted Content Discovery |
| **DAG** | Data Access Governance |
| **DSPM** | Data Security Posture Management |
| **DLP** | Data Loss Prevention |
| **PIM** | Privileged Identity Management |
| **B2B** | Collaboration entre entreprises (invités Entra ID) |
| **ROT** | Redundant, Obsolete, Trivial (contenu à nettoyer) |
| **ToU** | Conditions d'utilisation (Terms of Use) |
