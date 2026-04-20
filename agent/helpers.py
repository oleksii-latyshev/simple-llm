import json

from openai import OpenAI

from agent.config import OLLAMA_HOST, SYSTEM_PROMPT_PATH


def load_system_prompt() -> str:
    try:
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a helpful assistant answering questions based on tools."


def parse_tool_args(raw: str) -> dict:
    try:
        args = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return {k: v for k, v in args.items() if v is not None}


def create_client() -> OpenAI:
    return OpenAI(base_url=f"{OLLAMA_HOST}/v1", api_key="ollama")
