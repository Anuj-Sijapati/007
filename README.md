# 007 — full-stack dev agent for Claude Code

`/007` orchestrates a task across four domain subagents — frontend, backend, devops,
database. It understands the project first (existing repo: scans it; empty dir: asks
requirements), dispatches only the subagent(s) a task actually needs, and gates any
remote/destructive command (`git push`/`pull`, `terraform apply`, `kubectl apply/delete`,
`docker push`, migrations, deletes) behind an explicit y/n confirmation.

## Install

**If you use the VS Code extension**, install as a plugin, from an actual terminal (not
the VS Code chat panel — `/plugin` doesn't work there):

```
claude
```
then inside the CLI:
```
/plugin marketplace add Anuj-Sijapati/007
/plugin install 007@Anuj-Sijapati
```

Reload the VS Code window afterward. The VS Code extension's `/` autocomplete only lists
plugin-installed commands — personal skills copied into `~/.claude/skills/` never show up
there ([known limitation](https://github.com/anthropics/claude-code/issues/60728)), even
though they work fine in the CLI.

**If you only use the CLI**, either the plugin install above, or manual copy works too:

```
git clone https://github.com/Anuj-Sijapati/007.git /tmp/007
cp -r /tmp/007/skills/007 ~/.claude/skills/
cp /tmp/007/agents/007-*.md ~/.claude/agents/
rm -rf /tmp/007
```

Either way, start a **new session** after installing — skills load at session start, not
mid-session.

## Usage

```
/007 add a health check endpoint
/007 scaffold a basic REST API
/007 add an endpoint and wire up the frontend form for it
```

The orchestrator writes/reads `PROJECT_CONTEXT.md` in the target project's root to avoid
re-scanning the project on every run.

## License

MIT
