# agent007 — full-stack dev agent for Claude Code

`/agent007` orchestrates a task across six subagents — frontend, backend, devops,
database, security, tester. It understands the project first (existing repo: scans it;
empty dir: asks requirements), dispatches only the subagent(s) a task actually needs, and
gates any remote/destructive command (`git push`/`pull`, `terraform apply`,
`kubectl apply/delete`, `docker push`, migrations, deletes) behind an explicit y/n
confirmation.

After implementation: changes touching a trust boundary (endpoints, input handling, auth,
queries, uploads, config, deps) automatically get a security audit — injection, auth gaps,
secrets, vulnerable deps, misconfig — and critical findings are fixed and re-checked before
reporting done. Changed logic without test coverage gets tests written and run. A separate
`/agent007-review` skill checks cross-domain seams (frontend calls vs real API shapes,
queries vs actual schema, app vs deploy config) plus a full security pass on the diff.

## Install

Works from any terminal, including the CLI used by the VS Code extension (the VS Code
chat panel's `/plugin` command doesn't work — run this from an actual terminal instead):

```
claude plugin marketplace add Anuj-Sijapati/007
claude plugin install agent007@agent007
```

Reload the VS Code window (or start a new CLI session) afterward — skills load at session
start, not mid-session. `/agent007:agent007` (or `/agent007` if it resolves unambiguously)
then shows up in autocomplete.

**Manual copy (CLI only — VS Code extension's autocomplete won't show it this way):**

```
git clone https://github.com/Anuj-Sijapati/007.git /tmp/agent007
cp -r /tmp/agent007/skills/agent007 ~/.claude/skills/
cp /tmp/agent007/agents/agent007-*.md ~/.claude/agents/
rm -rf /tmp/agent007
```

## Usage

```
/agent007 add a health check endpoint
/agent007 scaffold a basic REST API
/agent007 add an endpoint and wire up the frontend form for it
```

The orchestrator writes/reads `PROJECT_CONTEXT.md` in the target project's root to avoid
re-scanning the project on every run.

## License

MIT
