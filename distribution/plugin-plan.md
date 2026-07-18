# OpenAI plugin packaging plan

OpenAI's [plugin-building documentation](https://learn.chatgpt.com/docs/build-plugins) defines `.codex-plugin/plugin.json` as the required entry point and permits `skills/` at the plugin root. Package all five canonical skills together for convenient ChatGPT Work and Codex distribution only after the skill evaluations pass.

## Proposed package

```text
australian-legal-research-plugin/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    ├── australian-jurisdiction-checker/
    ├── australian-legal-source-curator/
    ├── australian-legal-research/
    ├── australian-legal-reviewer/
    └── australian-legal-research-team/
```

Generate or copy the five directories from this repository during packaging; never maintain a divergent plugin copy. The manifest should declare the skills path, plugin name/version/description, and only verified interface metadata. Do not add MCP servers, apps, hooks, or executable code without a concrete requirement and security review.

## Release gates

1. Validate all five `SKILL.md` files and links.
2. Run explicit, implicit, negative, and single-specialist trigger cases.
3. Run jurisdiction, source-quality, currency, and adversarial-review cases in Codex and the target ChatGPT workspace.
4. Confirm workspace data, web access, and administrator policy.
5. Pin a version, record source-register verification date, build the package from canonical files, and inspect the archive.
6. Publish through the approved marketplace/workspace route and rerun smoke tests from the installed cache.

This plan does not promise that the same plugin package installs in Hermes. Hermes distribution remains separate.
