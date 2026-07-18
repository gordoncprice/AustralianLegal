---
name: australian-legal-source-curator
description: Build an authoritative source plan for Australian legal research and assess source authority, currency, official status, and limitations. Use to locate preferred legislation, court, tribunal, regulator, gazette, and explanatory sources; do not use for a final legal answer or jurisdiction determination.
---

# Australian legal source curator

Create a source plan, not a substantive legal answer. Research the question's actual jurisdictions and subject matter; do not treat the bundled register as exhaustive or permanently current.

## Procedure

1. Take an issue and jurisdiction map as inputs. Identify the source types needed for each proposition.
2. Start with the official publisher for legislation, instruments, commencement, courts, tribunals, regulators, parliamentary materials, and explanatory documents.
3. Verify organisation names, URLs, official status, coverage, and update mechanisms during the task. Record the verification date.
4. Rank sources using [references/source-hierarchy.md](references/source-hierarchy.md). Use [references/official-source-register.md](references/official-source-register.md) as a researched starting point and update the plan when current official information differs.
5. Assess each candidate with [references/source-assessment-rubric.md](references/source-assessment-rubric.md): authority, authenticity, currency, completeness, relevance, citability, and access.
6. Distinguish law from regulator guidance and official from unofficial republication. Use AustLII and commentary for discovery or gap-filling, then trace material propositions to primary sources where available.
7. Include commercial databases only as optional aids. Never make paid access a condition of the plan.
8. Explain unavailable or unverified sources and propose a safe fallback.

## Output contract

```yaml
issue:
jurisdictions:
primary_sources:
official_secondary_sources:
case_law_sources:
currency_checks:
source_limitations:
verification_date:
```

For each source record publisher, jurisdiction, coverage, type, authority level, official status, typical use, limitations, preferred citation, and currency check.
