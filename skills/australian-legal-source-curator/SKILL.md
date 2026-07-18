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
4. Rank sources using the internal, non-numerical authority-weight framework in [references/source-hierarchy.md](references/source-hierarchy.md). Prefer the strongest reasonably available authority for each proposition. If a lower-weight source is proposed while a stronger relevant authority exists, record why.
5. Assess each candidate with [references/source-assessment-rubric.md](references/source-assessment-rubric.md): authority, authenticity, currency, completeness, relevance, citability, and access. For a negative proposition, assess whether the source set is authoritative and sufficiently complete to establish non-existence.
6. Distinguish law from regulator guidance and official from unofficial republication. Use AustLII and commentary for discovery or gap-filling, then trace material propositions to primary sources where available.
7. Include commercial databases only as optional aids. Never make paid access a condition of the plan.
8. Identify sources needed to detect material recent change, including amendments, commencement and transitional material, recent controlling or appellate authority, and regulator policy revisions where relevant.
9. Explain unavailable or unverified sources and propose a safe fallback. Use `not located in the sources checked` rather than `does not exist` unless an authoritative, sufficiently complete register or source establishes the negative claim.

## Output contract

```yaml
issue:
jurisdictions:
primary_sources:
official_secondary_sources:
case_law_sources:
authority_weight_assessment:
stronger_authority_check:
change_detection_sources:
currency_checks:
source_limitations:
verification_date:
source_completeness_confidence:
```

For each source record publisher, jurisdiction, coverage, type, authority level, official status, typical use, limitations, preferred citation, and currency check.
