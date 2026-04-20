from tools.read_document.schema import ReadDocumentArgs
from tools.read_document.handler import execute

TOOL_NAME = "read_document"
TOOL_DESCRIPTION = "Reads a fragment of a text file. Use this tool to study document contents. The default file to read is `data/test_document.txt`."
TOOL_ARGS_SCHEMA = ReadDocumentArgs

__all__ = ["TOOL_NAME", "TOOL_DESCRIPTION", "TOOL_ARGS_SCHEMA", "execute"]
