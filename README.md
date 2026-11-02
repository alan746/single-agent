# Paper Scout

Paper Scout is a command-line research agent built from scratch in Python, without an agent framework. Give it a topic, and it searches arXiv over several rounds, picks the most relevant papers, and saves a Markdown report.

I am building it in stages to learn how agents work, from the basic tool-calling loop to tracing, failure handling, and memory.

## How it works

1. You pass a research topic on the command line.
2. The model decides what to do next and can call two tools:
   - `arxiv_search` queries the arXiv API.
   - `write_file` saves the report inside `output/`.
3. The agent runs each tool call and sends the result back to the model.
4. The loop ends when the model finishes or a limit is reached, such as the step limit.

## Project stages

| Stage | Goal | Status |
| --- | --- | --- |
| **L1: Working agent** | Search with varied keywords, write a report with real papers, stop on its own, enforce a step limit, and block writes outside `output/` | Done |
| **L2: Reliable agent** | Add JSONL tracing, tests with a fake model, a cost budget, error recovery, recovery from truncated responses, and accurate paper metadata | In progress |
| **L3: Agent with memory** | Add persistent memory, context compression, the ability to resume a run, and reusable modules | Planned |

## Project structure

| Path | Purpose |
| --- | --- |
| `agent.py` | Runs the agent loop and calls the model |
| `tools.py` | Defines and implements the tools |
| `tracer.py` | Writes JSONL trace records (in progress) |
| `memory.py` | Placeholder for L3 |

The `output/` and `logs/` directories are created when needed and are not tracked by git.

## Getting started

These commands are for Windows PowerShell. You need Python 3.12 or later and an Anthropic API key.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the project root, and never commit it:

```text
ANTHROPIC_API_KEY=your_api_key
```

Run the agent, with quotes around any topic that contains spaces:

```powershell
python agent.py "LLM multi-agent cooperation"
```

Each run makes real API calls, so it uses your API credit.
