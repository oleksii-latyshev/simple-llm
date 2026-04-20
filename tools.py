from pydantic import BaseModel, Field

class ReadDocumentArgs(BaseModel):
    """Arguments for the document reading tool."""
    file_path: str = Field(..., description="Path to the text file to read.")
    offset: int = Field(0, description="Line number to start reading from (0-based).")
    limit: int = Field(50, description="Maximum number of lines to read at once.")

def read_document_tool(file_path: str, offset: int = 0, limit: int = 50) -> dict:
    """
    Читає фрагмент текстового файлу. 
    Використовуй цей інструмент, щоб детально вивчити контекст документа.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        total_lines = len(lines)
        snippet = lines[offset : offset + limit]
        
        return {
            "status": "success",
            "total_lines_in_file": total_lines,
            "showing_lines": f"{offset} to {offset + len(snippet)}",
            "content": "".join(snippet)
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}