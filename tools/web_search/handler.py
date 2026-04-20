from ddgs import DDGS


def execute(query: str, max_results: int = 5) -> dict:
    max_results = max(1, min(int(max_results), 10))

    try:
        with DDGS() as ddgs:
            raw_results = list(ddgs.text(query, max_results=max_results))

        if not raw_results:
            return {"status": "success", "results": [], "message": "No results found."}

        results = [
            {
                "title": r.get("title", ""),
                "snippet": r.get("body", ""),
                "url": r.get("href", ""),
            }
            for r in raw_results
        ]

        return {"status": "success", "results": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
