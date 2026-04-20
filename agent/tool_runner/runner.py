import json

from agent.tool_runner.discovery import discover_tools

# Built once at import time
_REGISTRY = discover_tools()


def get_tools_schema() -> list[dict]:
    return [entry["schema"] for entry in _REGISTRY.values()]


def execute_tool(name: str, args: dict) -> dict:
    entry = _REGISTRY.get(name)
    if entry is None:
        return {"status": "error", "message": f"Unknown tool: {name}"}
    return entry["module"].execute(**args)
