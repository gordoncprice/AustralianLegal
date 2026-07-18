---
name: australian-legal-research-team
description: Coordinate an end-to-end, independently reviewed Australian legal research workflow across jurisdiction, source, research, and reviewer roles. Use for substantive questions needing a final cited answer or memorandum; do not use for a narrow source list, jurisdiction map, draft-only review, or non-legal task.
---

# Australian legal research team

Coordinate the full workflow in [references/orchestration-workflow.md](references/orchestration-workflow.md). Provide research information, not legal advice, and scale the final response to the user's question.

## Host capability rule

If the host supports subagents, create bounded specialist roles for jurisdiction checking, source curation, substantive research, and independent review. Parallelise only independent work such as legislation/commencement, cases/treatment, guidance/enforcement, and Commonwealth/state overlap. Keep the reviewer separate from every researcher.

If subagents are unavailable, run the same roles sequentially. Preserve separate artefacts labelled `Jurisdiction assessment`, `Source plan`, `Researcher draft`, `Reviewer findings`, and `Final synthesis`. A single agent may change roles, but must complete and freeze the researcher draft before beginning the independent review pass.

If a specialist skill cannot be invoked directly, read that skill's `SKILL.md` and required references and apply them as the role definition. Never imply that a host invoked another skill when it did not.

## Required stages

1. Frame the factual, legal, and practical questions; identify missing facts and safe assumptions.
2. Run the jurisdiction-checker role.
3. Run the source-curator role and verify current official sources.
4. Run substantive research, dividing genuinely independent streams where useful.
5. Have the jurisdiction role audit the completed draft.
6. Give the independent reviewer the user's question, facts, assumptions, jurisdiction map, source plan, draft, citations, and unresolved issues. Do not ask it to approve.
7. Address every critical and major issue; resolve or disclose medium issues, remove unsupported claims, and reduce the relevant confidence dimension where verification remains incomplete.
8. Complete a final proposition audit after review and revision. For each material proposition check the supporting authority; exact support for the wording; overbreadth; missing exceptions or qualifications; currency; whether the source is law, guidance, or commentary; and whether revision introduced a new unsupported proposition. Do not deliver until this audit is complete.
9. Deliver the final answer using [references/final-answer-template.md](references/final-answer-template.md), adapted to scope. Prioritise core issues and place peripheral regimes under `Additional issues if relevant` only when the facts make them material.

Read [references/handoff-contracts.md](references/handoff-contracts.md) before delegating. Read [references/worked-example.md](references/worked-example.md) when planning a multi-jurisdiction employment or corporations-law task.

Ask follow-up questions only when a missing fact prevents responsible progress. Otherwise proceed with labelled assumptions. Include a research date and proportionate disclaimer in every substantive final answer.
