import json

from agent.config import MODEL_NAME, MAX_ITERATIONS, TEMPERATURE
from agent.tool_runner import get_tools_schema, execute_tool
from agent.helpers import load_system_prompt, parse_tool_args, create_client


def run_agent(user_query: str) -> str:
    client = create_client()
    tools_schema = get_tools_schema()

    messages = [
        {"role": "system", "content": load_system_prompt()},
        {"role": "user", "content": user_query},
    ]

    print(f"🕵️ Agent started. Task: {user_query}\n")

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"🔄 Iteration {iteration}...")

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools_schema,
            temperature=TEMPERATURE,
        )
        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("\n✅ Agent finished!")
            print("📝 Final answer:")
            print(message.content)
            return message.content

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = parse_tool_args(tool_call.function.arguments)
            print(f"  🛠️ {name}({args})")

            result = execute_tool(name, args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": name,
                "content": json.dumps(result, ensure_ascii=False),
            })

    print(f"\n⚠️ Iteration limit reached ({MAX_ITERATIONS}).")
    return messages[-1].content if messages else ""
