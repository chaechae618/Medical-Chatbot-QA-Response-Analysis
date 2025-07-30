import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

# OpenAI API 키를 가져옴
openai.api_key = os.getenv("OPENAI_API_KEY")

# FastAPI 앱을 생성함
app = FastAPI(debug=True)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ChatRequest 모델을 정의함
class ChatRequest(BaseModel):
    message: str
    temperature: float = 1

def request_user_info():
    # import requests
    # requests.get{"http://aip.xxx.com/user/info"}
    
    return """
    -Like Asia food
    - /like to travel to Spain
    - 30 years old.
"""


def get_planning_manual():
    return """
    - 30 years old man likes eating food.
    - 30 years old man likes walking.

"""

SYSTEM_MSG = f"""
You are a helpful assistant, Your name is Jini, 27 years old

Current User:
{request_user_info()}
              
Planning Manual:
{get_planning_manual()}
"""
      
#사용자의 intent 추출 함수
def classify_intent(msg):
    prompt = """Your job is to classify intent.
        
    Choose one of following intents:
    - travel_plan
    - curtomer_support
    - reservation
    
    User : {msg}
    Intent:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [
            {'role':'user','content':prompt},
        ],
    )
    return response.choices[0].message.content.strip()

# "/chat" 엔드포인트를 정의함
@app.post("/chat")
async def chat(req: ChatRequest):
    intent == classify_intent(req.message)
    if intent == "travel_plan":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
                    messages=[
                         {"role":"systems","contents":SYSTEM_MSG},
            {"role": "user", "content": req.message},
        ],
            temperature=req.temperature,
        )
        return {"message": response.choices[0].message.content}
    elif intent =="customer_surport":
        return {"message ": "Here is customer number"}
    elif intent == 'reservation':
        return {"message":"here is reservation number"}
        

# 서버를 실행함
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)