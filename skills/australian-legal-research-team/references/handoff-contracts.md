# Handoff contracts

Use these internally. Do not force structured data on the end user.

## Frozen research specification

```yaml
question:
material_facts:
assumptions:
event_date:
research_date:
jurisdictions:
court_and_tribunal_hierarchy:
material_issues:
material_propositions:
deliverable:
research_depth: focused | comprehensive
scope_changes:
```

## Shared internal research record

Keep this record internal and hand the same version forward.

```yaml
research_specification_version:
legislation_searched:
case_repositories_searched:
searches_completed:
  - issue:
    repository:
    query_or_method:
    filters_and_date_range:
    search_date:
    result_and_limit:
candidate_authorities:
selected_authorities:
  - authority:
    analytical_purpose:
    hierarchy_and_status:
    treatment_and_currency:
    pinpoint:
    verified_direct_link:
rejected_authorities:
  - authority:
    rejection_reason:
link_verification:
failed_checks:
unresolved_research_gaps:
targeted_supplementary_searches:
stopping_basis:
```

## Jurisdiction handoff

```yaml
question:
material_facts:
assumptions:
likely_jurisdictions:
possible_overlaps:
applicable_court_and_tribunal_hierarchy:
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
safe_to_proceed_conditionally:
conclusions_not_yet_safe:
```

## Source-plan handoff

```yaml
issue:
jurisdictions:
research_specification_version:
research_depth: focused | comprehensive
primary_sources:
official_secondary_sources:
case_law_sources:
ordered_case_discovery_plan:
authority_categories_not_required_with_reasons:
judgment_link_plan:
authority_weight_assessment:
stronger_authority_check:
change_detection_sources:
currency_checks:
source_limitations:
```

## Research handoff

```yaml
issue:
jurisdictions:
research_specification:
shared_internal_research_record:
legal_propositions:
authorities:
selected_case_functions:
judgment_link_verification:
proposition_citation_ledger:
contrary_authorities:
regulator_guidance:
change_detection:
source_dependency:
assumptions:
uncertainty_register:
  - issue:
    why_uncertain:
    potential_legal_impact:
    priority:
    information_required:
practical_next_steps:
conclusion_status: supported | provisional | conditional | unresolved | cannot safely conclude
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
gate_certification:
  jurisdiction:
  authority_discovery:
  authority_selection:
  citation_coverage:
  link_verification:
specific_deficiencies_requiring_targeted_research:
critical_issues:
major_issues:
minor_issues:
unsupported_claims:
jurisdiction_errors:
currency_risks:
authority_weight_defects:
case_discovery_coverage_defects:
case_selection_defects:
judgment_link_defects:
change_detection_defects:
source_dependency_risks:
issue_completeness_defects:
citation_defects:
proposition_coverage_defects:
required_revisions:
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
reviewer_new_propositions:
self_audit:
```

## Final proposition audit handoff

```yaml
material_propositions:
proposition_types_checked:
immediate_citation_coverage_checked:
strongest_authority_checked:
exact_support_checked:
judgment_links_and_metadata_checked:
case_analytical_functions_checked:
case_dumping_checked:
overbreadth_checked:
exceptions_checked:
currency_checked:
change_detection_checked:
legal_effect_labels_checked:
source_dependency_checked:
revision_introduced_claims_checked:
remaining_limitations:
complete:
```

## Quality-gate handoff

```yaml
strongest_authority_used:
no_stronger_authority_apparently_overlooked:
case_discovery_sufficient:
selected_cases_analytically_necessary:
no_cumulative_case_dumping:
material_propositions_supported:
citations_placed_at_point_of_support:
case_links_and_pinpoints_verified:
uncertainties_identified_and_prioritised:
assumptions_separated:
guidance_distinguished_from_law:
issue_completeness_review_complete:
proposition_audit_complete:
reviewer_self_audit_complete:
complete:
```

## Mandatory delivery-gate handoff

```yaml
gate_1_jurisdiction: pass | fail | not_verified
gate_2_authority_discovery: pass | fail | not_verified
gate_3_authority_selection: pass | fail | not_verified
gate_4_citation_coverage: pass | fail | not_verified
gate_5_link_verification: pass | fail | not_verified
gate_6_independent_review: pass | fail | not_verified
reviewer_certification:
delivery_permitted:
```

Each authority entry should contain a stable identifier or direct source URL, pinpoint, source type or legal-effect label, official status, hierarchy, analytical function, relevant date, currency/treatment check, and proposition supported. Every case entry must hyperlink the case name and neutral citation to the best accessible full-text judgment and record link, metadata and pinpoint verification. Each agent must identify tools used, failed checks, and material limitations.

Do not duplicate completed searches or verification across handoffs. A reviewer-requested supplementary search must identify the defective gate, issue, missing category or unsupported proposition and append its result to the shared internal research record.

Treat selected-case functions, link verification and proposition-citation ledgers as derived indexes into the shared internal research record. They must not become separate discovery records.

The proposition-citation ledger must cover every material legal or source-derived proposition, authority characterisation, application, qualification, uncertainty, authority-based confidence assessment and conclusion. Mark supplied facts separately. Label inferences and connect them to cited legal principles. Record citation placement and any unresolved support gap.

Rank uncertainty entries as `outcome-determinative`, `materially relevant`, or `secondary/evidentiary`. Ordinarily pass only the first two categories into the final answer. A handoff must place the material qualification before any conclusion that depends on it.
