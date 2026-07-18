# Hermes Desktop

Nous Research's [Hermes skills guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills/) documents local skills under `~/.hermes/skills/<category>/<skill>/SKILL.md`, compact skill metadata at session start, progressive loading through `skill_view`, natural-language requests to use a named skill, and installed-skill slash commands. The [Desktop guide](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) describes the desktop as using the same core skills and configuration.

Audit the five canonical directories for the installed Hermes version, then copy or symlink them beneath a category such as:

```text
~/.hermes/skills/legal/australian-legal-research/
~/.hermes/skills/legal/australian-legal-source-curator/
~/.hermes/skills/legal/australian-jurisdiction-checker/
~/.hermes/skills/legal/australian-legal-reviewer/
~/.hermes/skills/legal/australian-legal-research-team/
```

Start a new session or use the documented refresh mechanism, inspect the Skills pane/list, and test explicit natural-language invocation plus available slash commands. Tool names, subagent support, and external-directory configuration must be verified locally; the skills already define a sequential fallback.

Hermes plugins use a separate `plugin.yaml` plus Python registration system described in its [plugin documentation](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins). That format is not the OpenAI `.codex-plugin/plugin.json` format. Do not change the legal methodology or canonical front matter to mimic an undocumented Hermes behaviour. If a Hermes adapter is later needed, keep it thin and generated from the canonical skills.
