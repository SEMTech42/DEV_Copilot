# Access Concierge

Agent Copilot Studio qui, à partir d'un profil utilisateur, prépare et soumet les demandes d'accès (comptes, access packages Entra, rôles PIM éligibles, sites SharePoint, équipes Teams) via des circuits d'approbation existants.

- `profiles-matrix.md` : matrice profils → accès (source de vérité de l'agent)
- `agent-instructions.md` : instructions à coller dans Copilot Studio
- `mcp-server/SPEC.md` : spec du serveur MCP enveloppant Microsoft Graph / Entra

Principe : l'agent ne détient aucun rôle admin ; il crée uniquement des demandes validées par Entra.
