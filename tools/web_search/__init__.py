from tools.web_search.schema import WebSearchArgs
from tools.web_search.handler import execute

TOOL_NAME = "web_search"
TOOL_DESCRIPTION = "Searches the internet using DuckDuckGo. Returns titles, text snippets, and URLs of the top results. Use this tool to answer questions that require up-to-date or general knowledge from the web. Always include source URLs when citing web results."
TOOL_ARGS_SCHEMA = WebSearchArgs

__all__ = ["TOOL_NAME", "TOOL_DESCRIPTION", "TOOL_ARGS_SCHEMA", "execute"]
