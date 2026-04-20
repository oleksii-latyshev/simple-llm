from tools.query_products.schema import QueryProductsArgs
from tools.query_products.handler import execute

TOOL_NAME = "query_products"
TOOL_DESCRIPTION = "Searches for products in the database and returns their details and user feedback/reviews. Use this tool to answer questions about products, ratings, pros and cons."
TOOL_ARGS_SCHEMA = QueryProductsArgs

__all__ = ["TOOL_NAME", "TOOL_DESCRIPTION", "TOOL_ARGS_SCHEMA", "execute"]
