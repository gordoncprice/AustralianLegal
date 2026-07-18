---
title: Australian Legal Researcher
short_description: Provides authoritative research on Australian corporate and employment law.
category: legal/research
author: Hermes Agent
---
The **Australian Legal Researcher** skill is designed to provide high‑quality, evidence‑based research into Australian corporate and employment law for small‑to‑medium sized law firms.  It uses the official hierarchy of sources (statutes → case law → tribunals → regulators → secondary literature) and only cites legally binding authority as required.

## Usage

Invoke with a query and optional jurisdiction:
```hermes
$ hermes run australian-legal-researcher.run --query "What are directors' duties under the Corporations Act?" [--jurisdiction NSW]
```

The skill will return a markdown answer containing:

* Applicable jurisdiction  
* Relevant legislation (statutes or regulations)  
* Key binding case law with citations  
* Government guidance if applicable  
* A source reference list in citation format

The script is only a skeleton – it should be fleshed out with calls to `web_search`, `read_file` and other Hermes tools.
