# ChatGPT Desktop and ChatGPT Work

OpenAI's [Agent Skills documentation](https://learn.chatgpt.com/docs/build-skills) and [skills and plugins guidance](https://learn.chatgpt.com/docs/skills-and-plugins) describe the open skill format, automatic selection of installed skills, and explicit selection through supported skill/plugin mentions. Availability may depend on product rollout, desktop version, workspace policy, and administrator controls.

For individual authoring or testing, install a supported skill folder through the available ChatGPT skill surface and explicitly ask ChatGPT to use its exact name. Do not promise a custom slash command. For convenient workspace distribution of all five roles, package them as one plugin following [`plugin-plan.md`](plugin-plan.md); users can describe the task or explicitly choose the plugin/bundled skill through the supported UI.

The plugin should contain only these skills unless a real connector or MCP-backed app becomes necessary. Legal research can use the host's web tools and does not require a custom connector by default.

Before workspace release, an administrator should review:

- source access and web-research policy;
- data handling and confidentiality;
- skill and plugin availability controls;
- subagent support and sequential fallback;
- the independent-review boundary; and
- legal disclaimer and human-review expectations.

ChatGPT Desktop and Codex may ship different runtime versions. Re-run trigger and behavioural evaluations in each target surface.
