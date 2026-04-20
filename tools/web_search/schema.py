from pydantic import BaseModel, Field


class WebSearchArgs(BaseModel):
    """Arguments for web search."""
    query: str = Field(..., description="The search query to look up on the internet.")
    max_results: int = Field(5, description="Maximum number of search results to return (1-10).")
