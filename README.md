# 007 — full-stack dev agent for Claude Code

`/007` orchestrates a task across four domain subagents — frontend, backend, devops,
database. It understands the project first (existing repo: scans it; empty dir: asks
requirements), dispatches only the subagent(s) a task actually needs, and gates any
remote/destructive command (`git push`/`pull`, `terraform apply`, `kubectl apply/delete`,
`docker push`, migrations, deletes) behind an explicit y/n confirmation.

## Install

### From GitHub

```
/plugin marketplace add Anuj-Sijapati/007
/plugin install 007@Anuj-Sijapati
```

### Local development / before pushing

```
claude --plugin-dir /path/to/this/repo
```

or register the local path as a marketplace source:

```
/plugin marketplace add /path/to/this/repo
/plugin install 007@local
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

## Structure

```
.claude-plugin/plugin.json   plugin manifest
skills/007/SKILL.md          orchestrator: understand -> plan -> dispatch -> aggregate
agents/007-frontend.md       UI/components/styling
agents/007-backend.md        API/server logic
agents/007-devops.md         CI/deploy/infra, full Bash, confirm-gated on remote/destructive ops
agents/007-database.md       schema/migrations/queries, confirm-gated on migrations/deletes
```

## License

MIT
