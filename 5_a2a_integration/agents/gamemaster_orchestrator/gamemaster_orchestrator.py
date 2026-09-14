import uvicorn
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from strands import Agent
from strands_tools.a2a_client import A2AClientToolProvider
from tinydb import TinyDB, Query

app = FastAPI(title="D&D Game Master API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aws-samples.github.io",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class QuestionRequest(BaseModel):
    question: str


SYSTEM_PROMPT = """
You are a D&D Game Master orchestrator.

You have access to two specialized remote agents:

1. Rules Agent:
   http://127.0.0.1:8000

2. Character Agent:
   http://127.0.0.1:8001

Use the Rules Agent for D&D rules questions.
Use the Character Agent for creating, finding, or listing characters.
Do not invent information when one of the specialized agents can answer it.
"""


provider = A2AClientToolProvider(
    known_agent_urls=[
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8001",
    ]
)

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=provider.tools,
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "D&D Game Master",
        "endpoint": "/inquire",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/messages")
def get_messages():
    return agent.messages


@app.get("/user/{user_name}")
def get_user(user_name: str):
    # Same database used by the Character Agent
    db_path = Path(__file__).resolve().parents[2] / "characters.json"

    characters_db = TinyDB(db_path)
    query = Query()

    result = characters_db.search(
        query.name.test(lambda value: str(value).lower() == user_name.lower())
    )

    if not result:
        return {"error": f"Character with name '{user_name}' not found"}

    return result[0]


@app.post("/inquire")
async def inquire(request: QuestionRequest):
    response = await agent.invoke_async(request.question)
    return {"response": str(response)}


if __name__ == "__main__":
    print("🎲 Game Master running on http://127.0.0.1:8009")
    uvicorn.run(app, host="127.0.0.1", port=8009)
