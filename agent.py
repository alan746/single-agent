import json
import anthropic
from dotenv import load_dotenv
from tools import TOOLS, TOOLS_FUNCTION, arxiv_search
import sys

load_dotenv()

MODEL = "claude-haiku-5-5"
MAX_STEP = 10
client = anthropic.Anthropic()
SYSTEM_QUESTION ="Conduct multiple rounds of literature searches from different perspectives using varied keywords and search strategies. For each paper, provide its title, authors, publication year, link, and a brief explanation of its relevance to the research topic."
SYSTEM_MESSAGE = {"role": "system", "content": SYSTEM_QUESTION}


def call_model(messages: list[dict]):
    return client.messages.create(
        model = MODEL,
        max_tokens = 10000,
        output_config = {"effort": "high"},
        tools = TOOLS,
        messages = messages,
        system = SYSTEM_MESSAGE
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
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python agent.py "<research topic>"')
    question = sys.argv[1]
    messages = [{"role": "user", "content": question}]
    for i in range(MAX_STEP):
        response = call_model(messages)
        messages.append({"role": "assistant", "content": response.content})
        show(response, f"The {i+1} calling")
        if response.stop_reason == "tool_use":
            tool_result = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_result.append(run_tool(block))
            messages.append({"role": "user", "content": tool_result})
            for result in tool_result:
                print(f"{result['tool_use_id']} is used, is_error: {result['is_error']}, {len(result["content"])} characters ")
        else:
            if response.stop_reason == "end_turn":
                print("Task successfully done")
                return None
            if response.stop_reason == "max_tokens":
                print("Reaching maximum token usage")
                return None
            if response.stop_reason == "refusal":
                print("Llm denies thie request")
                raise SystemExit
            print("Unexpected stop reason")
            return None
    else:
        print("Reaching max step")
        return 

if __name__ == "__main__":
    run_model()


