import json
import anthropic
from dotenv import load_dotenv
from tools import TOOLS, TOOLS_FUNCTION, arxiv_search
import sys
from tracer import create_log, start_log, write_log
import time

load_dotenv()

MODEL = "claude-haiku-5-5"
MAX_STEP = 10
client = anthropic.Anthropic()
SYSTEM_QUESTION ="Conduct multiple rounds of literature searches from different perspectives using varied keywords and search strategies and keep 10 most relevant articles. For each paper, provide its title, authors, publication year, link, and a brief explanation of its relevance to the research topic. After searching, using write_file to store the result under output folder and end the program"
OUTPUT_CONFIG = {"effort": "high"}     
MAX_TOKENS = 20000


def call_model(messages: list[dict]):
    return client.messages.create(
        model = MODEL,
        max_tokens = MAX_TOKENS,
        output_config = OUTPUT_CONFIG,
        tools = TOOLS,
        messages = messages,
        system = SYSTEM_QUESTION
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

def using_tool(content):
    tool_result = []
    for block in content:
        if block.type == "tool_use":
            tool_result.append(run_tool(block))
    for result in tool_result:
        print(f"{result['tool_use_id']} is used, is_error: {result['is_error']}, {len(result["content"])} characters ")
    return tool_result

def response_format(response):
     content_log = []
     for block in response.content:
          content_log.append(block.model_dump())
     return content_log
    
def run_model():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python agent.py "<research topic>"')
    question = sys.argv[1]
    messages = [{"role": "user", "content": question}]
    create_log()
    start_log(MODEL, out_config = OUTPUT_CONFIG, topic = question, max_step = MAX_STEP)
    for i in range(MAX_STEP):
        response = call_model(messages)
        appending_message = []
        tool_result = []
        content_log = response_format(response)
        messages.append({"role": "assistant", "content": response.content})
        appending_message.append({"role": "assistant", "content": content_log})
        show(response, f"The {i+1} calling")
        if response.stop_reason == "tool_use":
            tool_result = using_tool(response.content)
            messages.append({"role": "user", "content": tool_result})
            appending_message.append({"role": "user", "content": tool_result})
        write_log(MODEL, OUTPUT_CONFIG, step = i + 1, messages = appending_message, 
                  stop_reason = response.stop_reason, input_tokens = response.usage.input_tokens, output_tokens = response.usage.output_tokens)
        if response.stop_reason == "tool_use":
            continue
        elif response.stop_reason == "end_turn":
            print("Task successfully done")
            return None
        elif response.stop_reason == "max_tokens":
            print("Reaching maximum token usage")
            return None
        elif response.stop_reason == "refusal":
            print("Llm denies thie request")
            raise SystemExit
        else:
            print("Unexpected stop reason")
            return None
    else:
        print("Reaching max step")
        return 

if __name__ == "__main__":
    run_model()


