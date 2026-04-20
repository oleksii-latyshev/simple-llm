from agent.core import run_agent

SOURCES = {"1": "auto", "2": "file", "3": "db"}


if __name__ == "__main__":
    print("📂 Select data source:")
    print("  1. auto (LLM decides)")
    print("  2. file (text documents only)")
    print("  3. db   (product database only)")
    choice = input("Your choice [1]: ").strip() or "1"
    source = SOURCES.get(choice, "auto")
    print(f"→ Source: {source}\n")

    query = input("❓ Enter your question: ")
    run_agent(query, source=source)
