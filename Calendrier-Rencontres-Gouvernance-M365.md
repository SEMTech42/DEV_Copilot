# Plan de travail et rencontres : 8 au 30 octobre 2026
**Gouvernance Microsoft 365 — priorité aux réalisations**
Version 2.0 (moins de rencontres, plus de réalisations ; à consolider avant transmission à ADM)

## Principe

Les rencontres sont réduites à **8 rencontres (environ 12 h)**, contre 18 (31 h) dans la version 1. Elles servent uniquement à décider, valider et débloquer. Le reste du temps est consacré à des **réalisations concrètes, documentées et mesurables** (10 lots, environ 38 jours-personne). Les décisions de détail se prennent par courriel ou dans les documents, avec un délai de réponse de 24 h.

## Hypothèses

- 16 jours ouvrables (8-9 oct., 13-16 oct., 19-23 oct., 26-30 oct.). **Le lundi 12 octobre est férié (Action de grâces)**, à confirmer.
- Les configurations techniques sont d'abord faites et testées en environnement de test, puis activées en production après validation du sponsor.
- Participants désignés par rôle ; noms à compléter.

## Légende des participants

| Code | Rôle |
|---|---|
| **SP** | Sponsor exécutif / représentant du comité exécutif ADM |
| **AR** | Architecte Microsoft 365 |
| **CP** | Chef de projet |
| **TI** | Équipe TI M365 (SharePoint, Teams, Entra, Power Platform) |
| **SEC** | Sécurité de l'information |
| **GD** | Gestion documentaire / conformité |
| **JUR** | Juridique / vie privée |
| **DIR** | Représentants des directions |

## 1. Rencontres (8, environ 12 h)

| # | Date proposée | Durée | Rencontre | Objectif | Participants requis |
|---|---|---|---|---|---|
| 1 | Jeu. 8 oct., 14 h | 1 h | Lancement | Confirmer portée, rôles, échéancier ; lancer les lots 1 et 2 | SP, AR, CP, TI, SEC |
| 2 | Ven. 9 oct., 9 h | 1 h 30 | Validation des décisions D1 à D18 | Faire approuver les règles (création bloquée, catalogue, externe, OneDrive, Copilot) pour pouvoir exécuter | SP, AR, CP, SEC, TI, DIR (2) |
| 3 | Ven. 16 oct., 10 h | 30 min | Point d'avancement no 1 | Suivre les lots, lever les blocages | SP, CP, AR |
| 4 | Mer. 21 oct., 9 h | 2 h | Atelier conception (portail, catalogue, gabarits) | Arbitrer en une séance : Power Apps ou ServiceNow, 5 types d'espaces, nommage, métadonnées des gabarits | AR, TI, GD, SEC, DIR (3) |
| 5 | Jeu. 22 oct., 13 h 30 | 2 h | Atelier sécurité et conformité (externe, Purview, identité) | Arbitrer en une séance : partage externe et invités, étiquettes, rétention, DLP, accès conditionnel | AR, SEC, TI, GD, JUR |
| 6 | Ven. 23 oct., 10 h | 30 min | Point d'avancement no 2 | Idem point no 1 | SP, CP, AR |
| 7 | Mar. 27 oct., 13 h 30 | 2 h | Revue des réalisations et démonstration | Démonstration du prototype portail, du gabarit et des rapports ; valider RACI, charte du comité et plan Copilot | AR, CP, TI, SEC, GD, DIR (3), SP |
| 8 | Ven. 30 oct., 10 h | 1 h | Comité exécutif ADM : décision d'exécution | Présenter les résultats, obtenir le « go » et les ressources de novembre | Comité exécutif ADM, SP, AR, CP |

Les rencontres 4 et 5 remplacent 9 ateliers de la version 1 : la préparation est faite par écrit avant la séance (documents d'options de 2 pages envoyés 48 h avant).

## 2. Réalisations (10 lots)

| Lot | Réalisation | Période | Responsable | Livrable mesurable | Critère de réussite | Effort (j-p) |
|---|---|---|---|---|---|---|
| 1 | **Inventaire du tenant** | 8 - 15 oct. | TI, AR | Rapport (sites, Groupes, Teams, propriétaires, invités, liens externes) en Excel | 100 % des sites et Groupes recensés ; sites orphelins et liens anonymes comptés | 4 |
| 2 | **Blocage de la création libre** | 13 - 16 oct. (test) ; 19 oct. (production) | TI | Paramètres Entra et SharePoint appliqués, message aux utilisateurs, processus transitoire | Aucune création libre dans l'audit pendant 2 semaines | 2 |
| 3 | **Prototype du portail de demande** | 13 - 26 oct. | TI, AR | Formulaire, flux d'approbation (gestionnaire, TI, sécurité) et provisioning Graph d'un espace de test | Une demande de bout en bout produit un espace conforme avec 2 propriétaires | 8 |
| 4 | **Gabarits Équipe et Projet (v1)** | 15 - 27 oct. | TI, GD | 2 gabarits en code (PnP) : bibliothèques, métadonnées, permissions, navigation, branding | Création automatisée en moins de 15 min, sans configuration manuelle | 6 |
| 5 | **Paramètres de partage externe** | 20 - 23 oct. | TI, SEC | Paramètres tenant appliqués en test (invités existants seulement, Anyone désactivé), processus d'approbation des invités rédigé | Zéro lien anonyme possible en test ; processus invité documenté | 3 |
| 6 | **Étiquettes de sensibilité et DLP** | 20 - 28 oct. | GD, SEC, TI | 4 étiquettes créées (non publiées), politique DLP en mode simulation, plan de rétention | Étiquettes validées par GD et JUR ; DLP en simulation sur SharePoint et OneDrive | 5 |
| 7 | **Rapport de surpartage initial (Copilot)** | 19 - 23 oct. | TI, SEC | Rapport SharePoint Advanced Management, liste des 20 sites prioritaires à corriger | Sites « Tout le monde » et liens larges identifiés ; priorités classées | 3 |
| 8 | **Accès conditionnel en mode rapport** | 20 - 28 oct. | SEC, TI | Politiques MFA, appareils conformes et invités créées en mode « rapport seulement » | Impact mesuré sur 5 jours avant activation | 2 |
| 9 | **Registre des espaces et détection des orphelins** | 19 - 26 oct. | TI | Registre initial (Dataverse ou liste), script mensuel de détection des sites sans 2 propriétaires | Registre aligné sur l'inventaire ; script testé | 2 |
| 10 | **Documentation et plan d'exécution** | 26 - 29 oct. | AR, CP | RACI, charte du comité, guide propriétaire, plan novembre à janvier | Documents approuvés à la rencontre 7 ; plan chiffré pour la rencontre 8 | 3 |

**Total réalisations : 38 jours-personne.** Pilotage et préparation des rencontres : environ 4 jours-personne. **Total : environ 42 jours-personne.**

## 3. Calendrier semaine par semaine

| Semaine | Rencontres | Réalisations en cours |
|---|---|---|
| 8-9 oct. | 1, 2 | Lot 1 (démarrage) |
| 13-16 oct. (lundi férié) | 3 | Lots 1 (fin), 2 (test), 3, 4 (démarrage) |
| 19-23 oct. | 4, 5, 6 | Lots 2 (production), 3, 4, 5, 6, 7, 8, 9 |
| 26-30 oct. | 7, 8 | Lots 3 à 10 (finalisation) ; démonstration ; décision ADM |

## 4. Charge à réserver (estimation)

| Ressource | Rencontres | Réalisations | Réservation conseillée |
|---|---|---|---|
| Architecte M365 | ~12 h | ~10 j | 80 % |
| Chef de projet | ~9 h | ~5 j | 50 % |
| TI M365 | ~8 h | ~25 j (2 à 3 personnes) | 100 % de 2 personnes |
| Sécurité | ~7 h | ~6 j | 30 % |
| Gestion documentaire / conformité | ~6 h | ~6 j | 30 % |
| Juridique / vie privée | 2 h | ~1 j | Ponctuel (rencontre 5) |
| Directions | ~4 h chacune | ~0,5 j | Ponctuel (rencontres 2, 4, 7) |
| Sponsor / comité exécutif | ~6 h | — | Rencontres 1, 2, 3, 6, 7, 8 |

## 5. Ce qui est livré le 30 octobre

1. Création libre bloquée en production.
2. Inventaire complet du tenant et rapport de surpartage priorisé.
3. Prototype de portail fonctionnel (de la demande à l'espace créé).
4. Deux gabarits (Équipe, Projet) créés par code.
5. Paramètres de partage externe validés en test, processus invités documenté.
6. Étiquettes, DLP (simulation) et accès conditionnel (rapport) prêts à activer.
7. Registre des espaces initial et détection automatique des orphelins.
8. RACI, charte du comité, plan d'exécution novembre à janvier.

## 6. Suite (novembre à janvier, ordre de grandeur)

| Chantier | Effort estimé |
|---|---|
| Mise en production du portail et provisioning Graph | 10 à 15 j-p |
| 3 gabarits restants (Communication, Communauté, Extranet) | 6 à 9 j-p |
| Activation Purview (étiquettes, DLP, rétention) | 15 à 25 j-p |
| Assainissement du partage externe existant | 10 à 15 j-p |
| Nettoyage des accès avant Copilot | 20 à 40 j-p |

## Points à confirmer avant transmission

- Jours fériés et disponibilités réelles (lundi 12 octobre).
- Noms des participants par rôle et suppléants.
- Disponibilité de 2 à 3 personnes TI à temps plein pour les lots 1 à 9.
- Accès à un environnement de test (tenant de développement ou site de test) pour les lots 2 à 5.
- Format et disponibilité du comité exécutif le 30 octobre.
