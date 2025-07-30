import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

client = openai.Client(api_key = "")

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    temperature: float = 1

response = client.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"What can you do?"},
    ],
    temperature=1,
    n=4,
)


app.post("/chat")
def chat(req: ChatRequest):
    response = client.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": req.message},
        ],
        temperature=req.temperature,
    )
    return {"message": response.choices[0].message.content}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app,host="0.0.0.0",port=8000)