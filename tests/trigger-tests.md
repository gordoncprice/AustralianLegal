# Trigger tests

Run all cases once with exact `$skill-name` invocation and once through natural-language matching where applicable.

| Case | Expected selection | Trigger distinction |
|---|---|---|
| `single-source-specialist` | Source curator only | Preferred official sources and currency method, no substantive answer |
| `remote-cross-border-worker` | Jurisdiction checker only | Coverage map, no full research |
| `fabricated-citation-review` | Reviewer only | Existing draft and adversarial verification |
| `full-team-trigger` | Research team | End-to-end current cited memorandum |
| `negative-nonlegal-trigger` | None | Law-firm context is not a legal research task |
| `corporations-commonwealth` | Research team | Substantive answer requires source, research and review roles even if jurisdiction is primarily Commonwealth |

Pass requires the selected skill to follow its output contract and the host not to activate unnecessary package skills. The coordinator may apply specialist roles internally; distinguish that from metadata selecting every skill at task start.

Likely failures include descriptions that are too broad, “legal” keyword matching, the team activating for every narrow task, the researcher self-approving, and the reviewer conducting an entirely new answer without reporting draft defects.
