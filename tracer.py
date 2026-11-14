import time
import json
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = (Path(__file__).parent) / "logs"

path = None

def create_log():
    global path
    now = datetime.now().strftime("%Y-%m-%d %H%M%S-%f")
    path = OUTPUT_DIR / f"{now}.jsonl"
    path.parent.mkdir(parents = True, exist_ok = True)

def start_log(model: str, out_config: dict[str, str], topic: str, max_step: int):
    write_event("run_start", model = model, out_config = out_config, topic = topic, max_step = max_step)

def write_log(model: str, out_config: dict[str, str], cumulative_steps: int, cumulative_tokens: int, messages: list[dict], 
              stop_reason: str, input_tokens: int, output_tokens: int):
    write_event("model_call", cumulative_steps = cumulative_steps, model = model, out_config = out_config, cumulative_tokens = cumulative_tokens,
                messages = messages, 
                stop_reason = stop_reason, input_tokens = input_tokens, output_tokens = output_tokens)
    
def write_run_end(reason: str, cumulative_tokens: int, cumulative_steps: int):
    write_event("run_end", reason = reason, cumulative_tokens = cumulative_tokens, cumulative_steps = cumulative_steps)

def take_elements(f):
    initial_values = {}
    messages = []
    for line in f:
        line = json.loads(line)
        if line["event"] == "run_start":
            initial_values["topic"] = line["topic"]
            initial_values["max_step"] = line["max_step"]
            messages += [{"role": "user", "content": line["topic"]}]
        elif line["event"] == "model_call":
            messages+= line["messages"]
            initial_values["cumulative_tokens"] = line["cumulative_tokens"]
            initial_values["cumulative_steps"] = line["cumulative_steps"]
        elif line["event"] == "run_end":
            initial_values["done"] = True
    initial_values["messages"] = messages
    return initial_values

def resume(filename: str):
    global path
    initial_values = {}
    path = filename
    if filename == "":
        files = Path(OUTPUT_DIR).glob("*.jsonl")
        path = (sorted(files, key = lambda p: p.name))[-1]
    with open(path, "r", encoding= "utf-8") as f:
        initial_values = take_elements(f)
    return initial_values

def write_resume():
    write_event("resume")
    return None

def write_event(event: str, **fields):
    time_stamp = datetime.now().isoformat()
    record = {"event": event, "time_stamp": time_stamp, **fields}
    with open(path, "a", encoding= "utf-8") as f:
        f.write(json.dumps(record) + "\n")


