from pydantic import BaseModel, Field

class ReadDocumentArgs(BaseModel):
    """Аргументы для инструмента чтения документа."""
    file_path: str = Field(..., description="Шлях до текстового файлу, який потрібно прочитати.")
    offset: int = Field(0, description="Номер рядка, з якого почати читання.")
    limit: int = Field(50, description="Максимальна кількість рядків для читання за один раз.")

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