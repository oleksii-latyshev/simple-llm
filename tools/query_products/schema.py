from pydantic import BaseModel, Field
from typing import Optional


class QueryProductsArgs(BaseModel):
    """Arguments for querying products and their feedback."""
    product_name: Optional[str] = Field(
        None,
        description="Product name (or part of it) to search for. Leave empty to list all products.",
    )
    include_feedback: bool = Field(
        True,
        description="Whether to include user feedback/reviews for the products.",
    )
