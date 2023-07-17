import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from agent.conversation_agent import agent_chain

app = FastAPI()


class ChatRequest(BaseModel):
    human_message: str
    history: list[str]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/chat')
async def chat(chat_request: ChatRequest):
    return agent_chain.run(chat_request.human_message)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
