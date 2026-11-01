import requests
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
import json
import time
from pathlib import Path

BASE_URL = "http://export.arxiv.org/api/"
ATOM = "{http://www.w3.org/2005/Atom}"
MIN_INTERVAL = 3.0
OUTPUT_DIR = Path("output")

last_request_time = 0.0

TOOLS = [
    {
        "name": "arxiv_search",
        "description": 
            "return arxiv_id, published, authors, link, title and summary for each article " +
            "based on the research topic and max number of search result" +
            "If results are irrelevant or too few, call it again with different keywords.",
        "input_schema":{
                        "type": "object",
                        "properties" : {
                            "query": {"type": "string", 
                                      "description": "arXiv search query using field prefixes, e.g. abs:\"multi-agent\" AND abs:cooperation"},
                            "max_results": 
                            {"type": "integer", "description": "maximum number of search result would return"}
                            },
                        "required": ["query", "max_results"]
                        }
    },
    {
        "name": "write_file",
        "description": "Creating file under output filefolder based on the given filename and content",
        "input_schema": {
            "type": "object",
            "properties":{
                "filename": {"type": "string",
                             "description": "Name of the file we want to create"},
                "content": {"type": "string",
                            "description": "Content we want to put on the file"}
            },
            "required": ["filename", "content"]
        }
    }
]
@dataclass
class Paper:
    arxiv_id: str
    published: str
    authors: list[str]
    link: str
    title: str
    summary: str

def _arxiv(query: str, max_results: int) -> list[Paper]:
    papers = []
    global last_request_time 
    now = time.time()
    if((now - last_request_time) < MIN_INTERVAL):
        time.sleep(MIN_INTERVAL-(now - last_request_time))
    last_request_time = time.time()
    response = requests.get(
        BASE_URL + "query",
        params = {"search_query" : query, "max_results" : max_results},
        timeout = 30
    )
    response.raise_for_status()
    root = ET.fromstring(response.text)
    for entry in root.findall(ATOM + "entry"):
        url = entry.findtext(ATOM + "id")
        arxiv_id = url.split("/abs/")[-1]
        published = entry.findtext(ATOM + "published")
        links = entry.find(ATOM + "link")
        link = links.get("href")
        title = entry.findtext(ATOM + "title")
        summary = entry.findtext(ATOM + "summary")
        authors = []
        for author in entry.findall(ATOM + "author"):
            authors.append(author.findtext(ATOM + "name"))
        paper = Paper(arxiv_id, published, authors, link, title, summary)
        papers.append(paper)
    return papers

def _result_format(papers: list[Paper]) -> str:
    result_with_correct_format = []
    for paper in papers:
        result_with_correct_format.append(asdict(paper))
    return json.dumps(result_with_correct_format)

def arxiv_search(query: str, max_results: int) -> str:
    papers = _arxiv(query, max_results)
    return _result_format(papers)
        
def write_file(filename: str, content: str) -> str:
    path = OUTPUT_DIR / filename
    path.parent.mkdir(parents = True, exist_ok = True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    result = f"Write on {str(path)}, content is {content}"
    return result

TOOLS_FUNCTION = {"arxiv_search": arxiv_search,
                  "write_file": write_file}

if __name__ == "__main__":
    print(arxiv_search("all:multiagent", 2))