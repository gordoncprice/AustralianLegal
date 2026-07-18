---
name: australian-jurisdiction-checker
description: Determine which Australian Commonwealth, state, territory, national, applied, or overlapping legal regimes may govern a matter and audit a draft for jurisdiction errors. Use for jurisdiction mapping or missing-fact analysis; do not use alone for full substantive research or source curation.
---

# Australian jurisdiction checker

Provide legal research assistance, not legal advice. Never infer the governing law from a keyword or the user's location.

## Procedure

1. Restate the question and extract the parties, relationships, conduct, dates, locations, operational footprint, company registration/business activity, and employee work location.
2. Identify missing facts that could change the governing regime. Continue on clearly labelled assumptions when useful research remains possible.
3. Consider Commonwealth constitutional or statutory coverage, national schemes, referrals, exclusions, applied laws, uniform/model laws, and local state or territory regimes.
4. Map every relevant state and territory, including cross-border connections and public-sector or local-government exceptions.
5. Check concurrent operation, inconsistency, displacement, choice-of-law, enforcement, forum, and territorial reach issues without resolving constitutional questions beyond the verified authorities.
6. Separate likely, additionally possible, and excluded or unlikely regimes. Explain the reason for each.
7. State the recommended research scope, unresolved questions, warnings, and confidence.
8. When auditing a draft, verify every cited law and conclusion against the map; flag national-scheme exceptions and unsupported jurisdiction assumptions.

Read [references/jurisdiction-framework.md](references/jurisdiction-framework.md) for the decision framework, [references/states-and-territories.md](references/states-and-territories.md) for jurisdiction prompts, and [references/conflict-and-overlap-checks.md](references/conflict-and-overlap-checks.md) for overlap review.

## Output contract

Return:

```yaml
question:
material_facts:
assumptions:
likely_jurisdictions:
possible_overlaps:
excluded_jurisdictions:
missing_facts:
confidence:
research_warnings:
recommended_research_scope:
```

Use `high`, `moderate`, or `preliminary/low` confidence and explain the basis. Do not deliver a final substantive legal conclusion.
