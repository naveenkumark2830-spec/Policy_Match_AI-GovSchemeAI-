from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from src.app import GovernmentSchemeAssistant
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store one assistant per user session
assistants = {}


assistant = GovernmentSchemeAssistant()

class ChatRequest(BaseModel):
    session_id: str
    message: str
    language: str = "English"

@app.post("/chat")
async def chat(request: ChatRequest):

    print("\n========== CHAT REQUEST ==========")
    print("SESSION ID:", request.session_id)
    try:
        print("MESSAGE:", request.message)
    except Exception:
        try:
            print("MESSAGE:", request.message.encode('utf-8', errors='ignore'))
        except Exception:
            print("MESSAGE: [Contains non-ASCII characters]")
    print("LANGUAGE:", request.language)

    # Create assistant if session is new
    if request.session_id not in assistants:
        assistants[request.session_id] = GovernmentSchemeAssistant()

    assistant = assistants[request.session_id]

    response = assistant.process_message(
        request.message,
        language=request.language
    )
    

    print("\n========== RESPONSE ==========")
    try:
        print(response[:500])  # first 500 chars
    except Exception:
        try:
            print(response[:500].encode('utf-8', errors='ignore'))
        except Exception:
            print("[Response contains non-ASCII characters]")
    print("================================\n")

    
    return {
        "session_id": request.session_id,
        "response": response
    }

@app.get("/new-session")
async def new_session():

    session_id = str(uuid.uuid4())

    assistants[session_id] = GovernmentSchemeAssistant()

    print("NEW SESSION CREATED:", session_id)

    return {
        "session_id": session_id
    }