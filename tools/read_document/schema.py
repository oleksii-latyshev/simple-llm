from pydantic import BaseModel, Field


class ReadDocumentArgs(BaseModel):
    """Arguments for the document reading tool."""
    file_path: str = Field(..., description="Path to the text file to read.")
    offset: int = Field(0, description="Line number to start reading from (0-based).")
    limit: int = Field(50, description="Maximum number of lines to read at once.")
