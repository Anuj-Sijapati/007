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

agent007 runs *inside* Claude Code (it's a set of skills and subagents), so Claude Code is
required. If you don't have it yet, that's **Step 1** below — the whole thing takes about a
minute from scratch.

### Step 1 — Install Claude Code (skip if you already have it)

Claude Code needs [Node.js 18+](https://nodejs.org). Then, in a terminal:

```
npm install -g @anthropic-ai/claude-code
```

Start it once and sign in (needs a Claude account — free or paid):

```
claude
```

Follow the login prompt, then type `/exit` to return to your shell.

### Step 2 — Install agent007

In **any terminal**, run these two commands:

```
claude plugin marketplace add Anuj-Sijapati/007
claude plugin install agent007@agent007
```

That's it. Restart Claude Code and type `/agent007` to use it.

### Where to run Step 2, per editor

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

## Using a non-Anthropic model (Cerebras, Qwen, DeepSeek, local, etc.)

agent007 is pure markdown — it doesn't care which model runs it. To use it with a
non-Anthropic provider, you point the **Claude Code harness** at that provider through a
gateway; agent007 needs no changes and installs exactly as above.

Easiest path is [`claude-code-router`](https://github.com/musistudio/claude-code-router)
(open-source proxy that maps Claude Code's requests to Cerebras/OpenAI-compatible/local
models):

```
npm install -g @musistudio/claude-code-router
ccr code            # starts Claude Code routed through your configured provider
```

Configure your Cerebras (or other) API key and model in the router's config, then install
agent007 into that session the same way. Alternatives: [LiteLLM proxy](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models)
or [Bifrost](https://github.com/maximhq/bifrost), both exposing an Anthropic-compatible
endpoint you set via `ANTHROPIC_BASE_URL`.

> **Honest caveat.** agent007's whole design leans on reliable tool-calling and subagent
> dispatch. Anthropic models do this well; many non-Anthropic models (smaller Llama/Qwen
> variants) call tools less reliably, so subagent dispatch and the security/test passes may
> misfire or get skipped. It runs — but expect the strongest results on Claude models.
> This is a property of the model, not something a plugin can fix. Anthropic does not
> officially support routing Claude Code to non-Claude models.

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
