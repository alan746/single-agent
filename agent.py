import json
import anthropic
from dotenv import load_dotenv
from tools import TOOLS, TOOLS_FUNCTION, arxiv_search

load_dotenv()

MODEL = "claude-haiku-5-5"
MAX_STEP = 10
client = anthropic.Anthropic()

def call_model(messages: list[dict]):
    return client.messages.create(
        model = MODEL,
        max_tokens = 10000,
        output_config = {"effort": "high"},
        tools = TOOLS,
        messages = messages
    )


def show(response, title: str):
    print(f"\n==== {title} =====")
    print("Stop reason:", response.stop_reason)
    for block in response.content:
        if block.type == "text":
            print(f"[text] {block.text}")
        elif block.type == "tool_use":
            print(f"[tool_use] id = {block.id} name = {block.name} input = {block.input}")
        else:
            print(f"[thinking]")

def run_tool(block):
    func = TOOLS_FUNCTION.get(block.name)
    try:
        if func is None:
            raise ValueError(f"No {block.name}such tool exist")
        content = func(**block.input)
        is_error = False
    except Exception as e:
        content = f"ERROR: {e}"
        is_error = True
    return {
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": content,
        "is_error": is_error
    }

    
def run_model():
    question = input()
    messages = [{"role": "user", "content": question}]
    for i in range(MAX_STEP):
        response = call_model(messages)
        messages.append({"role": "assistant", "content": response.content})
        show(response, f"The {i+1} calling")
        if response.stop_reason == "end_turn":
            print("Task successfully done")
            return None
        if response.stop_reason == "max_tokens":
            print("Reaching maximum token usage")
            return None
        if response.stop_reason == "refusal":
            print("Llm denies thie request")
            raise SystemExit
        tool_result = []
        for block in response.content:
            if block.type == "tool_use":
                tool_result.append(run_tool(block))
        if tool_result != []:
            messages.append({"role": "user", "content": tool_result})
        for result in tool_result:
            print(f"{result['tool_use_id']} is used, is_error: {result['is_error']}")

if __name__ == "__main__":
    run_model()


