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

You need [Claude Code](https://claude.com/claude-code) installed. Then, in **any
terminal**, run these two commands:

```
claude plugin marketplace add Anuj-Sijapati/007
claude plugin install agent007@agent007
```

That's it. Restart Claude Code and type `/agent007` to use it.

### Where to run the two commands, per editor

The commands are the same everywhere — only *where* you type them differs:

| Editor | Where to run | After install |
|--------|--------------|---------------|
| **Terminal / CLI** | Your normal shell | Start a new `claude` session |
| **VS Code** | Integrated terminal (`` Ctrl+` ``) — **not** the chat box | Reload window (`Ctrl/Cmd+Shift+P` → "Reload Window") |
| **Cursor** | Integrated terminal (`` Ctrl+` ``) — **not** the chat box | Reload window (`Ctrl/Cmd+Shift+P` → "Reload Window") |
| **JetBrains (IntelliJ/PyCharm/etc)** | Built-in terminal tab | Restart the IDE |

> **Why the terminal and not the chat box?** In the VS Code / Cursor extensions the
> `/plugin` command only works from a real terminal, not the chat input. Run the two
> commands in the terminal once, reload, and `/agent007` then appears in the chat box
> normally.

### Updating later

```
claude plugin update agent007@agent007
```

### Uninstalling

```
claude plugin uninstall agent007@agent007
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
