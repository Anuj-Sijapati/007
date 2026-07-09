---
name: agent007-review
description: Cross-domain integration review for work done by agent007 subagents. Checks the seams between layers — frontend calls match backend API shapes, backend queries match actual schema, deploy config matches app requirements — plus a security pass. Use when the user says "/agent007-review", after a multi-domain agent007 task, or before merging agent007 work.
---

# agent007-review — integration seam review

Single-domain checks (does the endpoint work, does the component render) are each
subagent's own job. This skill checks what nobody owns: **the seams between domains.**

## Scope

Review the current diff (`git diff` against the base branch, or the files changed in the
just-finished agent007 task). Read `PROJECT_CONTEXT.md` for conventions.

## Seam checks

Work through the seams that exist in this diff — skip pairs with no changed surface:

1. **Frontend ↔ backend** — every API call in changed frontend code hits a route that
   actually exists, with the right method; request/response field names match exactly
   (not camelCase on one side, snake_case on the other, unless a transform layer handles
   it); frontend error handling covers the error statuses the backend actually returns;
   no frontend assumption of a field the backend doesn't send.
2. **Backend ↔ database** — queries/ORM calls reference tables and columns that exist in
   the schema/migrations as of this diff; new columns the backend writes are in a
   migration; nullable columns are handled as nullable in code; transactions used where
   a multi-write sequence must be atomic.
3. **App ↔ devops** — env vars the app reads are declared in deploy/CI config (and
   vice versa: no dead config); exposed ports match; healthcheck endpoints referenced in
   config exist in the app; build commands in CI match the project's actual scripts.
4. **Migration ordering** — code that depends on a schema change must not deploy before
   the migration runs; flag any change where deploying code-first breaks.

## Security pass

Dispatch the `agent007-security` subagent (via the Agent tool) on the changed files.
Always — not just when the diff "looks security-relevant"; the point of the pass is
catching what didn't look relevant. Pass it only the changed file list plus what the
change was supposed to do.

## Report

One line per finding: `seam/security — file:line — problem — fix`. Severity-ranked,
security findings first. If a finding needs a code change, name which domain subagent
should fix it. End with a verdict line: `REVIEW: clean` or `REVIEW: N findings`.
No praise, no padding — clean diff gets a two-line report.
