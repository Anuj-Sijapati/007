# 007 — full-stack dev agent for Claude Code

`/007` orchestrates a task across four domain subagents — frontend, backend, devops,
database. It understands the project first (existing repo: scans it; empty dir: asks
requirements), dispatches only the subagent(s) a task actually needs, and gates any
remote/destructive command (`git push`/`pull`, `terraform apply`, `kubectl apply/delete`,
`docker push`, migrations, deletes) behind an explicit y/n confirmation.

## Install

```
/plugin marketplace add Anuj-Sijapati/007
/plugin install 007@Anuj-Sijapati
```

Scope defaults to `user` — installs globally across all your projects.

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
