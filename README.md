# agent007

**A full-stack developer agent for your IDE.** Give it a task; it understands your project,
does the work across frontend, backend, devops, and database, then security-reviews and
tests what it changed before reporting back.

Works in **VS Code, Cursor, JetBrains IDEs, and the terminal** — anywhere you can run
[Claude Code](https://claude.com/claude-code), the engine it plugs into. Install once, use
`/agent007` in every project.

---

## What it does

- **Understands first.** On an existing project it scans the stack, structure, and
  conventions into a `PROJECT_CONTEXT.md`; on an empty folder it asks what you want to
  build. Later runs reuse that file instead of re-scanning, so it stays cheap.
- **Dispatches only what's needed.** A backend-only task calls only the backend subagent —
  no idle work, no wasted tokens.
- **Verifies its own work.** Each subagent builds/tests/dry-runs before reporting done —
  no "done" on code that doesn't run.
- **Security by default.** Any change touching a trust boundary (endpoints, input, auth,
  queries, uploads, config, deps) gets an automatic audit — injection, auth gaps, exposed
  secrets, vulnerable deps, misconfig. Critical findings are fixed and re-checked.
- **Tests what it changes.** New logic without coverage gets focused tests written and run.
- **Asks before anything risky.** Remote or destructive commands — `git push`/`pull`,
  `terraform apply`, `kubectl apply/delete`, `docker push`, migrations, deletes — pause for
  an explicit y/n first.

## What's inside

| Type | Name | Role |
|------|------|------|
| Skill | `/agent007` | Orchestrator — understands, plans, dispatches, runs the security + test passes, reports |
| Skill | `/agent007-review` | Cross-domain seam review (frontend↔API, backend↔schema, app↔deploy) + security pass on a diff |
| Subagent | `agent007-frontend` | UI, components, styling — reads Figma links to match designs exactly |
| Subagent | `agent007-backend` | API routes, server & business logic |
| Subagent | `agent007-devops` | CI, containers, deploy, infra-as-code |
| Subagent | `agent007-database` | Schema, migrations, queries |
| Subagent | `agent007-security` | Read-only vulnerability review |
| Subagent | `agent007-tester` | Writes and runs tests for changed code |

## Install

agent007 runs inside Claude Code, so Claude Code is required. From scratch it's about a
minute.

### Step 1 — Install Claude Code *(skip if you already have it)*

Needs [Node.js 18+](https://nodejs.org). In a terminal:

```
npm install -g @anthropic-ai/claude-code
```

Start it once and sign in (a Claude account, free or paid), then `/exit` back to your shell:

```
claude
```

### Step 2 — Install agent007

In **any terminal**, run:

```
claude plugin marketplace add Anuj-Sijapati/007
claude plugin install agent007@agent007
```

Restart Claude Code and type `/agent007`. Done.

### Per-editor notes

Same two commands everywhere — only *where* you run them differs:

| Editor | Run Step 2 in | Then |
|--------|---------------|------|
| **Terminal / CLI** | Your shell | Start a new `claude` session |
| **VS Code** | Integrated terminal (`` Ctrl+` ``) — **not** the chat box | Reload window (`Ctrl/Cmd+Shift+P` → "Reload Window") |
| **Cursor** | Integrated terminal (`` Ctrl+` ``) — **not** the chat box | Reload window (`Ctrl/Cmd+Shift+P` → "Reload Window") |
| **JetBrains** (IntelliJ, PyCharm, …) | Built-in terminal tab | Restart the IDE |

> **Why the terminal, not the chat box?** In the VS Code / Cursor extensions the `/plugin`
> command only works from a real terminal. Run the two commands there once, reload, and
> `/agent007` shows up in the chat box normally.

### Update / uninstall

```
claude plugin update agent007@agent007
claude plugin uninstall agent007@agent007
```

## Usage

```
/agent007 add a health check endpoint
/agent007 scaffold a basic REST API
/agent007 add an endpoint and wire up the frontend form for it
```

Point it at a Figma URL in a frontend task and it fetches the real design to match spacing,
color, and typography instead of guessing.

## Using a non-Anthropic model (Cerebras, Qwen, DeepSeek, local, …)

agent007 is pure markdown — it doesn't care which model runs it. To use a non-Anthropic
provider, point the Claude Code harness at it through a gateway; agent007 needs no changes
and installs exactly as above.

Easiest path is [`claude-code-router`](https://github.com/musistudio/claude-code-router), an
open-source proxy mapping Claude Code's requests to Cerebras / OpenAI-compatible / local
models:

```
npm install -g @musistudio/claude-code-router
ccr code            # launches Claude Code routed through your configured provider
```

Set your provider's API key and model in the router config, then install agent007 the same
way. Alternatives: [LiteLLM proxy](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models)
or [Bifrost](https://github.com/maximhq/bifrost), both exposing an Anthropic-compatible
endpoint you point to via `ANTHROPIC_BASE_URL`.

> **Caveat, honestly:** agent007 leans on reliable tool-calling and subagent dispatch.
> Claude models do this well; smaller non-Anthropic models often call tools less reliably,
> so subagent dispatch and the security/test passes may misfire or get skipped. It runs —
> but expect the strongest results on Claude. That's a model property, not something a
> plugin can fix, and Anthropic doesn't officially support routing to non-Claude models.

## License

MIT
