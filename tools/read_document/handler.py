def execute(file_path: str, offset: int = 0, limit: int = 50) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        total_lines = len(lines)
        snippet = lines[offset : offset + limit]

        return {
            "status": "success",
            "total_lines_in_file": total_lines,
            "showing_lines": f"{offset} to {offset + len(snippet)}",
            "content": "".join(snippet),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
