"""MCP server exposing the AI concepts cheat sheet to any MCP-capable client.

Run: uv run --with mcp python server.py
"""

from pathlib import Path

from mcp.server.fastmcp import FastMCP

CHEAT_SHEET = Path(__file__).resolve().parent.parent / "skills" / "ai-concepts" / "SKILL.md"

mcp = FastMCP("ai-concepts")


@mcp.tool()
def ai_concepts_cheat_sheet() -> str:
    """Return the AI concepts cheat sheet: LLMs, tokens, prompts, agents,
    subagents, skills, MCP, hooks, memory, RAG, embeddings, hallucination,
    temperature. Use when the user asks to explain AI terminology or how AI
    tooling concepts fit together."""
    text = CHEAT_SHEET.read_text()
    # strip YAML frontmatter
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    return text.strip()


if __name__ == "__main__":
    mcp.run()
