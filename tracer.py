import time
import json
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = (Path(__file__).parent) / "logs"

path = None

def create_log():
    global path
    now = time.strftime("%Y-%m-%d %H%M%S-%f")
    path = OUTPUT_DIR / f"{now}.jsonl"
    path.parent.mkdir(parents = True, exist_ok = True)

def start_log(model: str, out_config: dict[str, str], topic: str, max_step: int):
    write_event("run_start", model = model, out_config = out_config, topic = topic, max_step = max_step)

def write_event(event: str, **fields):
    time_stamp = datetime.now().isoformat()
    record = {"event": event, "time_stamp": time_stamp, **fields}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


