# Evaluation guide

These are host-run behavioural evaluations, not deterministic unit tests. For each case in `test-cases.yaml`, start with a fresh task, expose only the installed skills and stated prompt/fixtures, capture the selected skill(s), role artefacts, tools/sources, draft, review decision, revisions, and final answer, then score against the case.

Where a case contains `fixture_requirements`, create and freeze that raw fixture before the run. Keep the evaluator-only answer key outside the agent-visible workspace. Use only authentic legal citations and judgment links in fixtures; deliberately unsupported propositions must be plausible but must not depend on fabricated authority.

## Run order

1. Validate repository structure and YAML front matter.
2. Run `trigger-tests.md`, including negative and single-specialist cases.
3. Run `jurisdiction-tests.md` and `source-quality-tests.md` with web access enabled, including authority-weight, change-detection and source-dependency cases.
4. Run `review-tests.md` with frozen draft fixtures so reviewer independence and self-verification can be observed.
5. Repeat representative cases in sequential-only mode and, where supported, subagent mode.
6. Record host/version, date, source availability, result, deviations, and reviewer.

## Repeat-run determinism protocol

For each case marked `repeat_runs`, execute the exact prompt and fixtures in the stated number of fresh, independent tasks. Do not pass outputs or research records between runs. Hold the event date, research date, source availability, host configuration and installed skill versions constant. Preserve each run's internal research specification, shared research record, gate certification and final answer for evaluator comparison.

Compare normalised legal content, not prose. Require materially equivalent governing legislation and provisions, principal authorities, propositions, qualifications, exceptions, conclusions, citations and preferred direct links. Permit changes in sentence order, headings and style. Investigate every material difference and accept it only if a recorded source-access change, genuinely new authority, corrected error or changed specification explains it. A silently omitted issue or authority is a failure.

For anti-duplication cases, compare the handoffs and tool trace. Jurisdiction and source planning may identify sources; substantive discovery is executed once and recorded once. Reviewer source reopening and deficiency-specific checks are permitted. Repeated full searches or verification without a named deficiency fail.

## Repository validation

```sh
git status --short --branch
find . -maxdepth 6 -type f | sort
find skills -mindepth 1 -maxdepth 1 -type d | sort
find . -type f -name '*.py' -print
git diff --check
git diff --stat origin/main...HEAD
git diff origin/main...HEAD
```

Confirm exactly five first-level skill directories, substantive instructions and required `name`/`description` front matter. Search the working tree for unfinished-language patterns specified in the build brief and investigate every match. Confirm no executable launcher is required.

## Scoring

Score each dimension 0 (fail), 1 (partial), or 2 (pass): trigger accuracy, jurisdiction accuracy, case-discovery breadth, authority selection, issue completeness, source quality, proposition-level citation coverage, statute/case link and pinpoint integrity, change detection, legal currency, source-dependency analysis, reviewer independence, research-record reuse, proportionality, mandatory-gate completion, repeat-run legal-content stability, uncertainty handling, usefulness, and proportional agent/tool use. Any fabricated citation, central jurisdiction error, overlooked controlling authority, unacknowledged obsolete law, unsupported material conclusion, missing or wrong central statute/case link, unexplained material instability across identical runs, duplicated full research, failed mandatory gate surviving delivery, or critical review issue surviving delivery is an overall failure.

Some evaluations require live web access and cannot be fully executed through static file inspection. Record them as not run, never as passed, when the host cannot open and verify current sources.

The redundancy regressions must use the current authorised Commonwealth and Queensland compilations. Record the exact compilation dates checked. The mass-redundancy case must distinguish Centrelink notice, registered employee-association notification/consultation, award or enterprise-agreement consultation, and genuine-redundancy consequences. The Queensland-system case must test the exact application of ss 125–127 without importing the federal s 389 test.
