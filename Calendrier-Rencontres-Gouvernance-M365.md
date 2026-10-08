# Plan de travail et rencontres : 8 au 30 octobre 2026
**Gouvernance Microsoft 365 — adapté à la capacité réelle de l'équipe**
Version 3.0 (à consolider avant transmission à ADM)

## Équipe et capacité

| Rôle | Capacité | 8-9 oct. (2 j) | 13-16 oct. (4 j, lundi férié) | 19-23 oct. | 26-30 oct. | Total période |
|---|---|---|---|---|---|---|
| Architecte applicatif M365 (**AA**) | 30 h/sem. | 12 h | 24 h | 30 h | 30 h | **96 h** |
| Architecte technologique M365 (**AT**) | 30 h/sem. | 12 h | 24 h | 30 h | 30 h | **96 h** |
| Chargé de projet (**CP**) | 21 h/sem. | 8 h | 17 h | 21 h | 21 h | **67 h** |
| **Total équipe** | | 32 h | 65 h | 81 h | 81 h | **259 h** |

Hypothèse : capacité répartie à parts égales sur les jours ouvrables ; le lundi 12 octobre est férié (Action de grâces, à confirmer). Le plan ci-dessous charge l'équipe à **253,5 h sur 259 h**, soit une marge de seulement 5,5 h.

**Constat :** la version précédente (environ 42 jours-personne) supposait une équipe TI plus large. À trois personnes, il faut réduire la portée : le gabarit Projet, la simulation DLP et la politique complète sont reportés en novembre. Les rencontres représentent 10,5 h (et non 12 h comme indiqué précédemment).

## Qui fait quoi

| Rôle | Responsabilités principales |
|---|---|
| **Architecte applicatif (AA)** | Prototype du portail (Power Apps, Power Automate, Graph), gabarits SharePoint/Teams, étiquettes et rétention, registre des espaces |
| **Architecte technologique (AT)** | Inventaire du tenant, blocage de la création libre, partage externe, rapport de surpartage, accès conditionnel, droits et identités applicatives |
| **Chargé de projet (CP)** | Pilotage, comités, communications, recette du prototype, spécifications du catalogue, coordination sécurité/gestion documentaire/juridique, documentation (RACI, charte, plan) |

## 1. Rencontres (8, 10,5 h au total)

Les trois membres de l'équipe participent à toutes les rencontres (10,5 h chacun).

| # | Date proposée | Durée | Rencontre | Objectif | Participants requis |
|---|---|---|---|---|---|
| 1 | Jeu. 8 oct., 14 h | 1 h | Lancement | Confirmer portée, rôles, échéancier ; lancer les lots 1 et 3 | Sponsor, AA, AT, CP, SEC |
| 2 | Ven. 9 oct., 9 h | 1 h 30 | Validation des décisions D1 à D18 | Faire approuver les règles pour pouvoir exécuter | Sponsor, AA, AT, CP, SEC, DIR (2) |
| 3 | Ven. 16 oct., 10 h | 30 min | Point d'avancement no 1 | Suivre les lots, lever les blocages | Sponsor, AA, AT, CP |
| 4 | Mer. 21 oct., 9 h | 2 h | Atelier conception (portail, catalogue, gabarits) | Arbitrer : Power Apps ou ServiceNow, 5 types d'espaces, nommage, métadonnées | AA, AT, CP, GD, SEC, DIR (3) |
| 5 | Jeu. 22 oct., 13 h 30 | 2 h | Atelier sécurité et conformité | Arbitrer : partage externe, étiquettes, rétention, accès conditionnel | AA, AT, CP, SEC, GD, JUR |
| 6 | Ven. 23 oct., 10 h | 30 min | Point d'avancement no 2 | Idem point no 1 | Sponsor, AA, AT, CP |
| 7 | Mar. 27 oct., 13 h 30 | 2 h | Revue des réalisations et démonstration | Démonstration du prototype, du gabarit et des rapports ; valider RACI et charte | AA, AT, CP, TI, SEC, GD, DIR (3), Sponsor |
| 8 | Ven. 30 oct., 10 h | 1 h | Comité exécutif ADM : décision d'exécution | Présenter les résultats, obtenir le « go » et les ressources de novembre | Comité ADM, Sponsor, AA, AT, CP |

Préparation écrite : documents d'options de 2 pages envoyés 48 h avant les rencontres 4 et 5 ; décisions de détail par courriel sous 24 h.

## 2. Réalisations (10 lots, 198 h pour l'équipe)

| Lot | Réalisation | Période | Livrable mesurable | AA | AT | CP | Total |
|---|---|---|---|---|---|---|---|
| 1 | **Inventaire du tenant** | 8 - 15 oct. | Rapport : 100 % des sites et Groupes recensés, orphelins et liens anonymes comptés | 4 h | 17 h | — | 21 h |
| 2 | **Blocage de la création libre** | Test 13-16 ; prod. 19 oct. | Paramètres Entra et SharePoint, message aux utilisateurs ; 0 création libre pendant 2 semaines | — | 8 h | 4 h | 12 h |
| 3 | **Prototype du portail** | 8 - 27 oct. | Formulaire, flux d'approbation et création d'un espace de test conforme (2 propriétaires) ; recette | 30 h | 8 h | 6 h | 44 h |
| 4 | **Gabarit Équipe (v1)** | 15 - 27 oct. | 1 gabarit en code, création en moins de 15 min ; spécification du gabarit Projet | 20 h | 4 h | 8 h | 32 h |
| 5 | **Paramètres de partage externe** | 20 - 23 oct. | Anyone désactivé en test, processus d'approbation des invités documenté | 2 h | 10 h | 3 h | 15 h |
| 6 | **Étiquettes et rétention** | 20 - 28 oct. | 4 étiquettes créées (non publiées), plan de rétention et plan DLP validés | 10 h | 8 h | 6 h | 24 h |
| 7 | **Rapport de surpartage (Copilot)** | 19 - 23 oct. | Rapport SAM et liste des 20 sites prioritaires | 3 h | 9 h | — | 12 h |
| 8 | **Accès conditionnel en mode rapport** | 20 - 28 oct. | 3 politiques (MFA, appareils, invités), impact mesuré sur 5 jours | — | 10 h | — | 10 h |
| 9 | **Registre des espaces et orphelins** | 13 - 26 oct. | Registre (liste SharePoint) aligné sur l'inventaire, script de détection testé | 6 h | 3 h | — | 9 h |
| 10 | **Documentation et plan d'exécution** | 26 - 29 oct. | RACI, charte du comité, guide propriétaire, plan novembre à janvier | 3 h | 2 h | 14 h | 19 h |
| | **Total réalisations** | | | **78 h** | **79 h** | **41 h** | **198 h** |

## 3. Bilan de charge

| Poste | AA | AT | CP | Total |
|---|---|---|---|---|
| Réalisations (lots 1 à 10) | 78 h | 79 h | 41 h | 198 h |
| Rencontres (8) | 10,5 h | 10,5 h | 10,5 h | 31,5 h |
| Préparation des ateliers et de la démonstration | 6 h | 6 h | — | 12 h |
| Comptes rendus, suivi et communications | — | — | 12 h | 12 h |
| **Charge planifiée** | **94,5 h** | **95,5 h** | **63,5 h** | **253,5 h** |
| Capacité | 96 h | 96 h | 67 h | 259 h |
| **Marge** | **1,5 h** | **0,5 h** | **3,5 h** | **5,5 h** |

### Charge par semaine (architectes et chargé de projet)

| Semaine | AA (cap. 12 / 24 / 30 / 30) | AT (cap. 12 / 24 / 30 / 30) | CP (cap. 8 / 17 / 21 / 21) | Lots dominants |
|---|---|---|---|---|
| 8-9 oct. | 12 h | 12 h | 8 h | 1 (inventaire), 3 (cadrage portail) |
| 13-16 oct. | 23,5 h | 24 h | 15 h | 1, 2 (test), 3, 4, 9 |
| 19-23 oct. | 30 h | 30 h | 19 h | 2 (prod.), 3, 4, 5, 6, 7, 8 |
| 26-30 oct. | 29 h | 29,5 h | 21,5 h | 3 à 10 (finalisation, démonstration) |

## 4. Appui requis hors équipe (environ 48 h)

| Ressource | Appui | Heures |
|---|---|---|
| Sécurité | Rencontres 1, 2, 4, 5, 7 ; revue des lots 5, 7, 8 | ~20 h |
| Gestion documentaire / conformité | Rencontres 4, 5, 7 ; taxonomie et rétention (lot 6) ; spécifications du gabarit | ~17 h |
| TI (administration) | Droits d'administration, fenêtres de changement, lots 2 et 9, rencontre 7 | ~8 h |
| Juridique / vie privée | Rencontre 5 ; validation de la rétention | ~3 h |
| Directions | Rencontres 2, 4, 7 | ~4 h chacune |
| Sponsor / comité exécutif | Rencontres 1, 2, 3, 6, 7, 8 | ~6 h |

## 5. Ce qui est livré le 30 octobre

1. Création libre bloquée en production.
2. Inventaire du tenant et rapport de surpartage priorisé.
3. Prototype de portail fonctionnel (de la demande à l'espace de test créé).
4. Gabarit Équipe créé par code ; gabarit Projet spécifié.
5. Partage externe validé en test, processus invités documenté.
6. Étiquettes créées (non publiées), plans de rétention et DLP validés ; accès conditionnel en mode rapport.
7. Registre des espaces et détection des orphelins.
8. RACI, charte du comité, plan d'exécution novembre à janvier.

## 6. Reporté en novembre (hors capacité de l'équipe d'octobre)

- Gabarit Projet en code, puis Communication, Communauté, Extranet.
- DLP en simulation puis en application.
- Intégration ServiceNow (si l'option B est retenue).
- Mise en production du portail et assainissement du partage externe existant.

## 7. Suite (novembre à janvier, ordre de grandeur)

| Chantier | Effort estimé |
|---|---|
| Mise en production du portail et du provisioning Graph | 10 à 15 j-p |
| 4 gabarits restants (Projet, Communication, Communauté, Extranet) | 8 à 12 j-p |
| Activation Purview (étiquettes, DLP, rétention) | 15 à 25 j-p |
| Assainissement du partage externe existant | 10 à 15 j-p |
| Nettoyage des accès avant Copilot | 20 à 40 j-p |

À 3 personnes (environ 12 jours-personne par semaine pour l'équipe), cela représente plus de 4 mois : prévoir du renfort TI ou un phasage plus long.

## Risques

- **Marge de 5,5 h seulement** : tout retard sur le prototype du portail (lot 3) ou sur l'inventaire (lot 1) décale la démonstration du 27 octobre. Arbitrage de repli : reporter le lot 9 ou la recette du lot 3.
- **Dépendances externes** : droits d'administration, environnement de test et disponibilités sécurité / gestion documentaire pour les ateliers des 21 et 22 octobre.
- **Décision tardive entre Power Apps et ServiceNow** : à trancher au plus tard à la rencontre 4 (21 octobre), sinon le prototype porte sur Power Apps par défaut.

## Points à confirmer avant transmission

- Disponibilité réelle de l'équipe (lundi 12 octobre férié, heures hebdomadaires de 30 h et 21 h).
- Environnement de test et droits d'administration pour l'architecte technologique.
- Noms des participants par rôle et suppléants.
- Format et disponibilité du comité exécutif le 30 octobre.
