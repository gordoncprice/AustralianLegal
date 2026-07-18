---
name: australian-legal-source-curator
description: Build an authoritative source plan for Australian legal research and assess source authority, currency, official status, and limitations. Use to locate preferred legislation, court, tribunal, regulator, gazette, and explanatory sources; do not use for a final legal answer or jurisdiction determination.
---

# Australian legal source curator

Create a source plan, not a substantive legal answer. Research the question's actual jurisdictions and subject matter; do not treat the bundled register as exhaustive or permanently current.

## Responsibility boundary

Design and validate the case-discovery plan, repositories, source hierarchy and access route. Specify how the researcher will find controlling, later, analogous, contrary and specialist authority and obtain judgment-level links. Do not decide which cases ultimately carry the analysis, apply cases to facts, or draft the substantive answer.

## Procedure

1. Take an issue and jurisdiction map as inputs. Identify the source types needed for each proposition.
2. Start with the official publisher for legislation, instruments, commencement, courts, tribunals, regulators, parliamentary materials, and explanatory documents.
3. Verify organisation names, URLs, official status, coverage, and update mechanisms during the task. Record the verification date.
4. Rank sources using the internal, non-numerical authority-weight framework in [references/source-hierarchy.md](references/source-hierarchy.md). Prefer the strongest reasonably available authority for each proposition. If a lower-weight source is proposed while a stronger relevant authority exists, record why.
5. Assess each candidate with [references/source-assessment-rubric.md](references/source-assessment-rubric.md): authority, authenticity, currency, completeness, relevance, citability, and access. For a negative proposition, assess whether the source set is authoritative and sufficiently complete to establish non-existence.
6. Distinguish law from regulator guidance and official from unofficial republication. Use AustLII and commentary for discovery or gap-filling, then trace material propositions to primary sources where available.
7. Include commercial databases only as optional aids. Never make paid access a condition of the plan.
8. Identify sources needed to detect material recent change, including amendments, commencement and transitional material, recent controlling or appellate authority, and regulator policy revisions where relevant.
9. For every material case-law issue, plan searches for controlling High Court authority; controlling or materially relevant intermediate appellate authority; later cases applying, explaining, distinguishing, limiting or qualifying leading authority; superior-court authority from the applicable jurisdiction; factually analogous decisions; significant contrary or competing authority; useful tribunal decisions; and recent cases that may alter the position. Do not impose a numerical quota. Require discovery to continue until defined hierarchy, treatment and factual searches produce only cumulative or immaterial additions.
10. Specify the preferred full-text link for each candidate repository: official court judgment or authorised court publication; otherwise an official government or judicial repository; otherwise AustLII, Jade or another reputable legal database. Reject search-result, summary, blog, news, AI-generated and commentary links when the judgment is accessible.
11. Explain unavailable or unverified sources and propose a safe fallback. Use `not located in the sources checked` rather than `does not exist` unless an authoritative, sufficiently complete register or source establishes the negative claim.

## Output contract

```yaml
issue:
jurisdictions:
primary_sources:
official_secondary_sources:
case_law_sources:
case_discovery_plan:
judgment_link_plan:
authority_weight_assessment:
stronger_authority_check:
change_detection_sources:
currency_checks:
source_limitations:
verification_date:
source_completeness_confidence:
```

For each source record publisher, jurisdiction, coverage, type, authority level, official status, typical use, limitations, preferred citation, and currency check.
