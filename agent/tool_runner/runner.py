import json

from agent.tool_runner.discovery import discover_tools

# Built once at import time
_REGISTRY = discover_tools()

# Map source modes to tool names
SOURCE_TOOLS = {
    "file": ["read_document"],
    "db": ["query_products"],
    "web": ["web_search"],
    "auto": list(_REGISTRY.keys()),
}


def get_tools_schema(source: str = "auto") -> list[dict]:
    allowed = SOURCE_TOOLS.get(source, SOURCE_TOOLS["auto"])
    return [entry["schema"] for name, entry in _REGISTRY.items() if name in allowed]


def execute_tool(name: str, args: dict) -> dict:
    entry = _REGISTRY.get(name)
    if entry is None:
        return {"status": "error", "message": f"Unknown tool: {name}"}
    return entry["module"].execute(**args)
