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
```

Each authority entry should contain a stable identifier or URL, pinpoint, source type, official status, relevant date, currency/treatment check, and proposition supported. Each agent must identify tools used, failed checks, and material limitations.
