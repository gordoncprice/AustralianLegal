---
name: australian-legal-curator
short_description: Maintains the authoritative source catalogue for Australian legal research.
category: knowledge/curation
author: Hermes Agent
---
The **Australian Legal Curator** skill gathers, evaluates, and stores trusted sources for each jurisdiction and practice area.  It keeps a structured catalogue file (`catalogue.yaml`) with metadata such as authority level, update frequency, and access URLs.

## Primary source types (ranked)
1. Commonwealth Acts & Regulations (AustLII, Office of the Parliamentary Counsel)  
2. State/Territory Acts & Regulations (state government portals, AustLII sub‑domains)  
3. Court decisions (High Court, Federal Court, Supreme Courts, appellate courts) via AUSTLII/legislation.dlg or other official databases  
4. Tribunal decisions (Fair Work Commission, state industrial commissions, administrative tribunals)  
5. Regulator guidance documents (ASIC, Safe Work Australia, Fair Work OMB, etc.)  
6. Authoritative secondary literature (Law Reform Commissions, Australian Law Journals, bar‑association practice notes)

The skill periodically runs scripts to:
* Pull the latest statutory updates via RSS/atom feeds or API endpoints where available
* Crawl court repositories for new decisions that meet a minimum citation threshold
* Check update dates against the catalogue and flag out‑of‑date entries

### Output
When requested, it returns the current `catalogue.yaml` in JSON format.  The catalogue is also available via Hermes memory to all running agents.
