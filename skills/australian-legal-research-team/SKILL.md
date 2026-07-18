---
name: australian-legal-research-team
description: Coordinate an end-to-end, independently reviewed Australian legal research workflow across jurisdiction, source, research, and reviewer roles. Use for substantive questions needing a final cited answer or memorandum; do not use for a narrow source list, jurisdiction map, draft-only review, or non-legal task.
---

# Australian legal research team

Coordinate the full workflow in [references/orchestration-workflow.md](references/orchestration-workflow.md). Provide research information, not legal advice, and scale the final response to the user's question.

## User control and mandatory safeguards

Honour user preferences about length, format, focus, visible workflow commentary, and whether the final answer contains a separate review section. These presentation choices do not waive internal legal quality controls.

Never agree to omit a material jurisdiction or system-coverage check, current-law and change checks, primary-authority or citation verification, correction of a false legal premise, material uncertainty disclosure, independent legal review, the final proposition audit, or the quality gate. If a user asks to disable a safeguard that is necessary to answer reliably, preserve the legitimate scope and presentation preference, explain the limit in one sentence, perform the minimum necessary check internally, and continue. For example: `I will keep the jurisdiction discussion brief, but it cannot be omitted because the applicable regime depends on it.`

Internal review is mandatory but need not be visible. If the user asks for no review or audit, provide a single integrated answer without a separate visible review section while retaining the normal internal verification process. Never say that review, audit, or verification will be omitted.

## Responsibility allocation

- **Jurisdiction checker:** determine jurisdiction, system coverage and the applicable court and tribunal hierarchy; do not select cases.
- **Source curator:** design and validate the broad case-discovery plan, repositories, authority hierarchy and judgment-link routes; do not apply or finally select cases.
- **Legal researcher:** execute discovery, verify and select materially useful cases, apply them, and draft proposition-level citations and judgment hyperlinks; do not self-approve.
- **Legal reviewer:** independently audit discovery breadth, selection, hierarchy, links, pinpoints, proposition coverage and citation placement; do not silently repair or approve defects.
- **Research team:** enforce the sequence, resolve review findings, complete the final coverage audit and deliver only the reviewed synthesis.

Use one frozen research specification and one shared internal research record for the whole task. Hand each artefact forward. No role may recreate a completed search or verification merely to demonstrate independence; the reviewer independently audits the record and reopens material sources.

## Host capability rule

If the host supports subagents, create only the bounded specialist roles required by the classified task. A material jurisdiction or source function may be brief or combined with intake, but independent review remains mandatory and separate from every researcher. Parallelise only independent work such as legislation/commencement, cases/treatment, guidance/enforcement, and Commonwealth/state overlap.

If subagents are unavailable, run the necessary roles sequentially. Preserve separate internal artefacts labelled `Jurisdiction assessment`, `Source plan`, `Researcher draft`, `Reviewer findings`, and `Final synthesis` when those roles are required. A single agent may change roles, but must complete and freeze the researcher draft before beginning the independent review pass.

If a specialist skill cannot be invoked directly, read that skill's `SKILL.md` and required references and apply them as the role definition. Never imply that a host invoked another skill when it did not.

## Required stages

1. Freeze the factual, legal and practical questions, missing facts, safe assumptions, event and research dates, jurisdictions, issue list, deliverable and research-depth class. Ask `What legal issues could reasonably arise from these facts?` and complete a proportionate issue-completeness review without adding irrelevant issues. Treat substantially identical inputs as the same research specification.
2. Run the jurisdiction-checker role whenever jurisdiction or system coverage may materially affect the answer. Triggers include Commonwealth/state or territory coverage, place of work, employer location or identity, contract formation, remote or interstate work, state entitlements, workers compensation, long service leave, discrimination, public-sector or local-government employment, constitutional-corporation status, referral arrangements, foreign elements, choice of law, or forum. Keep the step brief for simple matters. Do not assume a material jurisdiction silently or allow the user to disable this step.
3. Run the source-curator function to the extent needed and verify current official sources, authority weight, stronger-authority checks, change-detection sources, a broad case-discovery plan, and full-text judgment-link routes. A narrow, settled statutory question may use a focused primary-source check rather than a visible standalone source plan.
4. Run proportionate substantive research under the focused or comprehensive rule in [references/orchestration-workflow.md](references/orchestration-workflow.md). Update the shared internal research record with legislation and repositories searched, queries and limits, candidates, selected and rejected authorities with reasons, verified links, gaps and stopping basis. Require an analytical purpose for every selected case and a verified direct judgment link and pinpoint. For every material issue complete change detection, identify source dependency, and maintain a structured uncertainty register. When exact provisions are cited, distinguish each provision's function, application, thresholds, exclusions, entitlement, procedural requirement, and variation power rather than describing a provision range as one obligation. For redundancy research, treat federal ss 119, 121 and 122, instrument consultation, federal collective-dismissal provisions, and any applicable Queensland ss 125–127 as distinct inquiries and verify current primary text before use.
5. Have the jurisdiction role audit the completed draft.
6. Give the independent reviewer the frozen research specification, shared internal research record, jurisdiction map, source plan, draft, proposition-citation ledger, hyperlinks, pinpoints and unresolved issues. Do not ask it to approve. Permit only deficiency-specific supplementary research, recorded in the shared record.
7. Address every critical and major issue; resolve or disclose medium issues, remove unsupported claims, and reduce the relevant confidence dimension where verification remains incomplete.
8. Complete a final proposition audit after review and revision. For every material legal or source-derived proposition, authority characterisation, application, qualification, uncertainty and conclusion, check immediate citation coverage; strongest reasonably available authority; exact pinpoint support; judgment-level link and metadata; analytical purpose of each case; overbreadth; missing exceptions or qualifications; currency and material recent change; source dependency; legal-effect label; and whether revision introduced an unsupported proposition. Clearly distinguish supplied facts and labelled inferences. Do not deliver until this audit is complete.
9. Obtain the reviewer's explicit certification of Gates 1–5, then complete Gate 6 and the quality gate in [references/orchestration-workflow.md](references/orchestration-workflow.md). Do not deliver while any gate is `fail` or `not verified`.
10. Deliver one consolidated final answer using [references/final-answer-template.md](references/final-answer-template.md), adapted to scope. Do not expose or repeat specialist reports unless requested. Lead with a direct answer or action list for narrow or urgent tasks. Include only material caveats and useful immediate factual enquiries, documents, information needs, deadlines and procedural risks. Prioritise core issues and place peripheral regimes under `Additional issues if relevant` only when the facts make them material.

Read [references/handoff-contracts.md](references/handoff-contracts.md) before delegating. Read [references/worked-example.md](references/worked-example.md) when planning a multi-jurisdiction employment or corporations-law task.

Ask follow-up questions only when a missing fact prevents responsible progress. Otherwise proceed with labelled assumptions. If an unknown fact could materially change jurisdiction, entitlement, liability, procedure or remedy, state the provisional or conditional nature of the answer before the conclusion, not afterwards. Surface only outcome-determinative and materially relevant uncertainties, prioritised in that order. Include a research date and proportionate disclaimer in every substantive final answer.
