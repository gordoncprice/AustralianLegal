# Handoff contracts

Use these internally. Do not force structured data on the end user.

## Jurisdiction handoff

```yaml
question:
material_facts:
assumptions:
likely_jurisdictions:
possible_overlaps:
excluded_jurisdictions:
missing_facts:
confidence:
  jurisdiction_identification:
  legal_system_coverage:
  substantive_conclusion:
  source_completeness:
  factual_assumptions:
research_warnings:
```

## Source-plan handoff

```yaml
issue:
jurisdictions:
primary_sources:
official_secondary_sources:
case_law_sources:
currency_checks:
source_limitations:
```

## Research handoff

```yaml
issue:
jurisdictions:
legal_propositions:
authorities:
contrary_authorities:
regulator_guidance:
assumptions:
unresolved_questions:
draft_answer:
confidence:
  jurisdiction_identification:
  legal_system_coverage:
  substantive_conclusion:
  source_completeness:
  factual_assumptions:
```

## Review handoff

```yaml
decision:
critical_issues:
major_issues:
minor_issues:
unsupported_claims:
jurisdiction_errors:
currency_risks:
citation_defects:
required_revisions:
residual_uncertainty:
reviewer_new_propositions:
self_audit:
```

## Final proposition audit handoff

```yaml
material_propositions:
exact_support_checked:
overbreadth_checked:
exceptions_checked:
currency_checked:
legal_effect_labels_checked:
revision_introduced_claims_checked:
remaining_limitations:
complete:
```

Each authority entry should contain a stable identifier or URL, pinpoint, source type or legal-effect label, official status, relevant date, currency/treatment check, and proposition supported. Each agent must identify tools used, failed checks, and material limitations.
