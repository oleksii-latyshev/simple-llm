import json
import os
from openai import OpenAI
# Импортируем наш инструмент из соседнего файла tools.py
from tools import read_document_tool, ReadDocumentArgs

# 1. Подключение к локальной модели (Ollama)
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
client = OpenAI(
    base_url=f"{OLLAMA_HOST}/v1",
    api_key="ollama" 
)
MODEL_NAME = "llama3.2" # Та модель, которую ты скачал в docker-compose

# 2. Описание инструментов для LLM (JSON Schema)
# Мы передаем LLM инструкцию о том, КАКИЕ инструменты у нас есть
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_document_tool",
            "description": "Reads a fragment of a text file. Use this tool to study the contents of a document.",
            "parameters": ReadDocumentArgs.model_json_schema() # Pydantic генерирует схему автоматически
        }
    }
]

def run_agent(user_query: str):
    """Главный цикл работы агента."""
    
    # 3. Читаем системный промпт (инструкцию)
    try:
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            system_prompt = f.read()
    except FileNotFoundError:
        system_prompt = "You are a helpful assistant answering questions based on tools."

    # 4. Инициализация контекста (памяти агента)
    conversation_context = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]

    print(f"🕵️‍♂️ Агент начал работу. Задача: {user_query}\n")

    # 5. Главный цикл Perception-Action Loop
    iteration = 1
    while True:
        print(f"🔄 Итерация {iteration}...")
        
        # Шаг А: Запрос к "мозгу"
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=conversation_context,
            tools=TOOLS,
            temperature=0.1 # Низкая температура делает ответы более предсказуемыми
        )
        
        message = response.choices[0].message
        
        # Добавляем ответ модели в контекст, чтобы она помнила свой ход мыслей
        conversation_context.append(message)

        # Шаг Б: Проверка - хочет ли модель вызвать инструмент?
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                
                # Защита от галлюцинаций: LLM может придумать несуществующий аргумент
                try:
                    tool_args = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError:
                    tool_args = {}

                # Убираем None-значения, чтобы сработали дефолты функции
                tool_args = {k: v for k, v in tool_args.items() if v is not None}

                print(f"🛠️ Модель запрашивает инструмент: {tool_name} с аргументами {tool_args}")

                # Шаг В: Выполнение инструмента
                if tool_name == "read_document_tool":
                    # Физически выполняем нашу Python-функцию
                    result = read_document_tool(**tool_args)
                else:
                    # Если модель придумала несуществующий инструмент
                    result = {"status": "error", "message": f"Unknown tool: {tool_name}"}
                
                # Шаг Г: Формируем результат и возвращаем его в контекст
                # Обрати внимание: мы всегда возвращаем dict (даже при ошибке)
                conversation_context.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": json.dumps(result, ensure_ascii=False)
                })
        else:
            # Шаг Д: Завершение работы
            # Если нет tool_calls, значит агент считает, что задача выполнена
            print("\n✅ Агент завершил работу!")
            print("📝 Финальный ответ:")
            print(message.content)
            break
            
        iteration += 1


if __name__ == "__main__":
    query = input("❓ Введите ваш вопрос: ")
    run_agent(query)
    question = "Прочитай файл test_document.txt и скажи, о чем в нем говорится?"
    run_agent(question)