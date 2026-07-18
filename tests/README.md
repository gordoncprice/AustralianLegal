# Evaluation guide

These are host-run behavioural evaluations, not deterministic unit tests. For each case in `test-cases.yaml`, start with a fresh task, expose only the installed skills and stated prompt/fixtures, capture the selected skill(s), role artefacts, tools/sources, draft, review decision, revisions, and final answer, then score against the case.

## Run order

1. Validate repository structure and YAML front matter.
2. Run `trigger-tests.md`, including negative and single-specialist cases.
3. Run `jurisdiction-tests.md` and `source-quality-tests.md` with web access enabled.
4. Run `review-tests.md` with frozen draft fixtures so reviewer independence and self-verification can be observed.
5. Repeat representative cases in sequential-only mode and, where supported, subagent mode.
6. Record host/version, date, source availability, result, deviations, and reviewer.

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

Score each dimension 0 (fail), 1 (partial), or 2 (pass): trigger accuracy, jurisdiction accuracy, source quality, citation traceability, legal currency, reviewer independence, uncertainty handling, usefulness, and proportional agent/tool use. Any fabricated citation, central jurisdiction error, unacknowledged obsolete law, or critical review issue surviving delivery is an overall failure.

Some evaluations require live web access and cannot be fully executed through static file inspection. Record them as not run, never as passed, when the host cannot open and verify current sources.

The redundancy regressions must use the current authorised Commonwealth and Queensland compilations. Record the exact compilation dates checked. The mass-redundancy case must distinguish Centrelink notice, registered employee-association notification/consultation, award or enterprise-agreement consultation, and genuine-redundancy consequences. The Queensland-system case must test the exact application of ss 125–127 without importing the federal s 389 test.
