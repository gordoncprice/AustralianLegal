# Codex

OpenAI's [skill-building documentation](https://learn.chatgpt.com/docs/build-skills) describes repository skills under `.agents/skills` from the working directory up to the repository root, personal skills under `~/.agents/skills`, and administrator skills under `/etc/codex/skills`. It also describes progressive loading, implicit selection from the description, explicit `$skill-name` mentions, and `/skills` in Codex CLI/IDE.

Keep this repository's canonical files under `skills/`. For local testing, create links rather than manual copies:

```sh
mkdir -p .agents/skills
for skill in skills/*; do ln -sfn "../../$skill" ".agents/skills/$(basename "$skill")"; done
```

Then start a new Codex task from the repository, inspect `/skills`, and test explicit and implicit prompts from `tests/test-cases.yaml`. A personal installation can link the absolute skill directories into `~/.agents/skills/`.

Do not claim `~/.codex/skills` as the public personal authoring path unless the installed Codex version documents it. Internal or older installations may expose other locations.

Example:

```text
$australian-legal-research-team Research whether the proposed termination may be a genuine redundancy, including the applicable Australian jurisdiction and current primary sources.
```

Subagent availability is host-dependent. The team skill must preserve the same staged workflow and independent review when it runs sequentially.
