---
name: australian-jurisdiction-checker
description: Determine which Australian Commonwealth, state, territory, national, applied, or overlapping legal regimes may govern a matter and audit a draft for jurisdiction errors. Use for jurisdiction mapping or missing-fact analysis; do not use alone for full substantive research or source curation.
---

# Australian jurisdiction checker

Provide legal research assistance, not legal advice. Never infer the governing law from a keyword or the user's location.

## Procedure

1. Restate the question and extract the parties, relationships, conduct, dates, locations, operational footprint, company registration/business activity, and employee work location.
2. Identify missing facts that could change the governing regime. Record each material gap in an uncertainty register with the issue, reason for uncertainty, potential legal impact, priority, and information required. Continue on clearly labelled assumptions when useful research remains possible.
3. Consider Commonwealth constitutional or statutory coverage, national schemes, referrals, exclusions, applied laws, uniform/model laws, and local state or territory regimes.
4. Map every relevant state and territory, including cross-border connections and public-sector or local-government exceptions.
5. Check concurrent operation, inconsistency, displacement, choice-of-law, enforcement, forum, and territorial reach issues without resolving constitutional questions beyond the verified authorities.
6. Separate likely, additionally possible, and excluded or unlikely regimes. Support exclusions and other negative propositions with sufficiently complete authoritative research; otherwise say what was not located or verified rather than asserting non-existence.
7. Prioritise the core issues. Put peripheral regimes under `additional_issues_if_relevant` and include taxation, privacy, licensing, payroll tax, or similar matters only when the facts make them material.
8. State the recommended research scope, unresolved questions, warnings, and separate confidence assessments for jurisdiction identification, legal-system coverage, substantive conclusion, source completeness, and factual assumptions. Distinguish confidence that a jurisdiction requires investigation from confidence that a particular law applies.
9. When auditing a draft, verify every cited law and conclusion against the map; flag national-scheme exceptions and unsupported jurisdiction assumptions.

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
uncertainty_register:
  - issue:
    why_uncertain:
    potential_legal_impact:
    priority:
    information_required:
confidence:
  jurisdiction_identification:
  legal_system_coverage:
  substantive_conclusion:
  source_completeness:
  factual_assumptions:
research_warnings:
recommended_research_scope:
additional_issues_if_relevant:
```

Use `high`, `moderate`, or `preliminary/low` for each confidence dimension and explain the basis. A jurisdiction map may be high confidence while ultimate legal coverage remains moderate or low. Do not deliver a final substantive legal conclusion.
