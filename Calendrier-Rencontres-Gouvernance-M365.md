# Plan de travail d'octobre et feuille de route de 6 mois
**Gouvernance Microsoft 365 — octobre 2026 à mi-avril 2027**
Version 4.0 (équipe de 3 ; projet d'environ 6 mois ; accès attendus vers le 15 octobre)

## Hypothèses

- Durée du projet : environ 6 mois, du 8 octobre 2026 au 16 avril 2027.
- **Les accès au tenant seront obtenus d'ici une semaine (vers le jeudi 15 octobre).** Avant cette date, le travail porte sur la conception et la préparation ; après, sur la configuration, l'inventaire et le prototype.
- Équipe : architecte applicatif (**AA**, 30 h/sem.), architecte technologique (**AT**, 30 h/sem.), chargé de projet (**CP**, 21 h/sem.), soit 81 h/semaine.
- Jours fériés (à confirmer) : lundi 12 octobre ; congés du 21 décembre au 1er janvier ; vendredi saint (2 avril).
- Les configurations sont d'abord testées en environnement de test puis activées en production après validation du sponsor.

## Partie 1 — Octobre 2026 (phase 0)

### Capacité d'octobre

| Rôle | 8-14 oct. (avant accès, 4 j) | 15-16 oct. (2 j) | 19-23 oct. | 26-30 oct. | Total |
|---|---|---|---|---|---|
| AA | 24 h | 12 h | 30 h | 30 h | **96 h** |
| AT | 24 h | 12 h | 30 h | 30 h | **96 h** |
| CP | 17 h | 8 h | 21 h | 21 h | **67 h** |
| **Équipe** | 65 h | 32 h | 81 h | 81 h | **259 h** |

### Rencontres (8, 10,5 h au total ; l'équipe de 3 participe à toutes)

| # | Date proposée | Durée | Rencontre | Objectif | Participants requis |
|---|---|---|---|---|---|
| 1 | Jeu. 8 oct., 14 h | 1 h | Lancement | Confirmer portée, rôles, échéancier, calendrier d'obtention des accès | Sponsor, AA, AT, CP, SEC |
| 2 | Ven. 9 oct., 9 h | 1 h 30 | Validation des décisions D1 à D18 | Faire approuver les règles pour pouvoir exécuter | Sponsor, AA, AT, CP, SEC, DIR (2) |
| 3 | Ven. 16 oct., 10 h | 30 min | Point d'avancement no 1 (accès reçus ?) | Confirmer les accès, lever les blocages | Sponsor, AA, AT, CP |
| 4 | Mer. 21 oct., 9 h | 2 h | Atelier conception (portail, catalogue, gabarits) | Arbitrer : Power Apps ou ServiceNow, 5 types d'espaces, nommage, métadonnées | AA, AT, CP, GD, SEC, DIR (3) |
| 5 | Jeu. 22 oct., 13 h 30 | 2 h | Atelier sécurité et conformité | Arbitrer : partage externe, étiquettes, rétention, accès conditionnel | AA, AT, CP, SEC, GD, JUR |
| 6 | Ven. 23 oct., 10 h | 30 min | Point d'avancement no 2 | Suivre les lots | Sponsor, AA, AT, CP |
| 7 | Mar. 27 oct., 13 h 30 | 2 h | Revue des réalisations et démonstration | Démonstration du prototype, du gabarit et des rapports | AA, AT, CP, TI, SEC, GD, DIR (3), Sponsor |
| 8 | Ven. 30 oct., 10 h | 1 h | Comité exécutif ADM : décision d'exécution | Résultats de la phase 0, feuille de route de 6 mois, ressources | Comité ADM, Sponsor, AA, AT, CP |

### Réalisations d'octobre (8 lots, 182 h)

| Lot | Réalisation | Période | Livrable mesurable | AA | AT | CP | Total |
|---|---|---|---|---|---|---|---|
| 1 | **Cadrage et décisions** | 8 - 16 oct. | Charte, décisions D1-D18 signées, plan de projet de 6 mois | 3 h | 3 h | 11 h | 17 h |
| 2 | **Spécifications (avant accès)** | 8 - 20 oct. | Portail (formulaire, flux, registre), catalogue et nommage, gabarits, brouillons de taxonomie d'étiquettes, de partage externe et d'accès conditionnel | 23 h | 7 h | 10 h | 40 h |
| 3 | **Préparation technique (avant accès)** | 8 - 16 oct. | Scripts d'inventaire et de rapport prêts ; liste des rôles et permissions demandés (moindre privilège) ; plan de bascule | — | 14 h | 2 h | 16 h |
| 4 | **Inventaire du tenant et rapport de surpartage** | 15 - 23 oct. | Inventaire 100 % des sites, Groupes, Teams, invités ; rapport SAM ; liste des 20 sites prioritaires | 4 h | 22 h | — | 26 h |
| 5 | **Blocage de la création libre** | Test 19-21 oct. ; prod. 26 oct. | Paramètres Entra et SharePoint, message aux utilisateurs ; 0 création libre pendant 2 semaines | — | 8 h | 4 h | 12 h |
| 6 | **Prototype du portail** | 16 - 30 oct. | Formulaire, flux d'approbation et création d'un espace de test conforme ; recette | 26 h | 8 h | 5 h | 39 h |
| 7 | **Gabarit Équipe (v1)** | 20 - 30 oct. | 1 gabarit en code, création en moins de 15 min | 14 h | 3 h | 3 h | 20 h |
| 8 | **Documentation** | 26 - 29 oct. | RACI, charte du comité, guide propriétaire | 2 h | 2 h | 8 h | 12 h |
| | **Total réalisations** | | | **72 h** | **67 h** | **43 h** | **182 h** |

Les lots 1 à 3 se font avant l'obtention des accès ; les lots 4 à 7 après.

### Bilan de charge d'octobre

| Poste | AA | AT | CP | Total |
|---|---|---|---|---|
| Réalisations | 72 h | 67 h | 43 h | 182 h |
| Rencontres (8) | 10,5 h | 10,5 h | 10,5 h | 31,5 h |
| Préparation des ateliers et de la démonstration | 6 h | 6 h | — | 12 h |
| Comptes rendus, suivi et communications | — | — | 12 h | 12 h |
| **Charge planifiée** | **88,5 h** | **83,5 h** | **65,5 h** | **237,5 h** |
| Capacité | 96 h | 96 h | 67 h | 259 h |
| **Marge** | **7,5 h** | **12,5 h** | **1,5 h** | **21,5 h** |

Charge par période (AA / AT / CP) : 8-14 oct. 24 h / 24 h / 17 h ; 15-16 oct. 12 h / 12 h / 8 h ; 19-23 oct. 27 h / 25 h / 20 h ; 26-30 oct. 25,5 h / 22,5 h / 20,5 h.

**Effet de l'obtention des accès :** la marge de 20 h des architectes absorbe environ 3 jours de retard. Au-delà du 20 octobre, le gabarit Équipe (lot 7) est reporté à novembre et la démonstration du 27 octobre porte sur les maquettes et les rapports.

### Ce qui est livré le 30 octobre

1. Décisions D1 à D18 signées et plan de projet de 6 mois.
2. Spécifications du portail, du catalogue, du nommage et des gabarits.
3. Inventaire du tenant et rapport de surpartage priorisé.
4. Création libre bloquée en production (sous réserve de la validation du sponsor).
5. Prototype de portail fonctionnel (création d'un espace de test).
6. Gabarit Équipe (v1) créé par code.
7. RACI, charte du comité, guide propriétaire.

## Partie 2 — Feuille de route de 6 mois

| Phase | Période | Objectifs et livrables clés | Charge estimée | Capacité équipe |
|---|---|---|---|---|
| **0. Cadrage et prototype** | 8 - 30 oct. | Voir partie 1 | 237,5 h | 259 h |
| **1. Bloquer et stabiliser** | 2 - 27 nov. | Portail en pilote (2 directions) ; gabarits Équipe et Projet ; registre des espaces ; partage externe en test ; accès conditionnel en mode rapport ; blocage en production confirmé | 252 h (~36 j-p) | 324 h |
| **2. Portail et gabarits** | 30 nov. - 15 janv. (congés 21 déc. - 1er janv.) | Portail en production avec provisioning Graph ; gabarits Communication, Communauté, Extranet ; OneDrive restrictif ; modèles Teams ; partage externe sécurisé (Anyone désactivé, processus invités) ; étiquettes publiées | 308 h (~44 j-p) | 405 h |
| **3. Purview et conformité** | 18 janv. - 26 fév. | DLP (simulation puis application) ; rétention et enregistrements ; audit et alertes ; revues d'accès ; assainissement du partage externe existant ; cycle de vie automatisé (orphelins, archivage) | 350 h (~50 j-p) | 486 h |
| **4. Préparation Copilot** | 1 - 31 mars | Nettoyage des accès ; SAM (RCD, RAC, politique d'inactivité) ; DSPM pour l'IA ; DLP pour Copilot ; pilote de 100 à 300 utilisateurs | 301 h (~43 j-p) | 365 h |
| **5. Déploiement et transfert** | 1 - 16 avr. | Déploiement par vagues ; formation ; comité de gouvernance en régime permanent ; transfert à l'exploitation ; bilan | 140 h (~20 j-p) | 186 h |
| **Total** | **8 oct. - 16 avr.** | | **≈ 1 589 h** | **≈ 2 025 h** |

L'utilisation planifiée est d'environ 78 % de la capacité ; les 22 % restants (environ 437 h) couvrent les congés, le support, les imprévus et les délais d'approbation. Ces estimations de novembre à avril sont des ordres de grandeur à affiner à la fin de la phase 0, avec les résultats de l'inventaire et du rapport de surpartage.

### Jalons et comités exécutifs ADM

| Date | Jalon |
|---|---|
| 30 oct. | Fin phase 0 : décision d'exécution |
| 27 nov. | Fin phase 1 : portail pilote, blocage confirmé |
| 15 janv. | Fin phase 2 : portail et gabarits en production |
| 26 fév. | Fin phase 3 : Purview et partage externe sécurisés |
| 31 mars | Fin phase 4 : feu vert au déploiement Copilot |
| 16 avr. | Fin phase 5 : bilan et transfert |

### Appui requis hors équipe (ordre de grandeur)

| Ressource | Octobre | Novembre à avril |
|---|---|---|
| Sécurité | ~20 h | ~6 h par semaine en moyenne |
| Gestion documentaire / conformité | ~17 h | ~5 h par semaine (pic en phase 3) |
| TI (administration) | ~8 h | ~4 h par semaine |
| Juridique / vie privée | ~3 h | Ponctuel (phase 3) |
| Directions et propriétaires de sites | ~4 h par rencontre | Revues d'accès et nettoyage (phase 4) |

## Risques

- **Accès au tenant** : l'obtention après le 15 octobre réduit la marge d'octobre ; au-delà du 20 octobre, report du gabarit Équipe. Les accès doivent être demandés avec les rôles précis préparés au lot 3.
- **Marge du chargé de projet de 1,5 h seulement** en octobre : toute tâche additionnelle (comités, comptes rendus) doit être arbitrée.
- **Décision Power Apps ou ServiceNow** : à trancher au plus tard à la rencontre 4 (21 octobre) ; sinon le prototype reste sur Power Apps.
- **Équipe de 3 personnes** pour 6 mois : absence d'un membre = retard direct ; prévoir un suppléant TI pour l'administration.
- **Nettoyage des accès avant Copilot** (phase 4) : dépend de la participation des propriétaires de sites ; à lancer dès la phase 3.

## Points à confirmer avant transmission

- Date réelle d'obtention des accès et liste des rôles accordés.
- Environnement de test (tenant de développement ou site de test).
- Congés de fin d'année, jours fériés et disponibilités réelles de l'équipe.
- Noms des participants par rôle et suppléants.
- Fréquence retenue des comités exécutifs ADM (un par fin de phase proposé).
