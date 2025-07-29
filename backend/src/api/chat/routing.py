from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage 
from api.db import get_session
from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessageSchema, SupervisorMessageSchema
from api.ai.agents import get_supervisor


router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


# /api/chats/recent/
# curl http://localhost:8080/api/chat/recent/
@router.get("/recent/")
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results


#HTTP POST -> paylaod = ("message": "hello world")
# curl -X POST -d '{"message": "hello world"}' -H "Content-Type: application/json" http://localhost:8080/api/chat/
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump() #pydantic -> dict
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    response = generate_email_message(payload.message)
    return response

@router.post("/supervisor/", response_model=SupervisorMessageSchema)
def chat_create_supervisor_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    supe = get_supervisor()
    msg_data = {
        "messages": [
            {"role": "user", 
            "content": f"{payload.message}"
            },
        ]
    }
    response = supe.invoke(msg_data)
    if not response:
        raise HTTPException(status_code=500, detail="No response from supervisor")
    if not response.get('messages'):
        raise HTTPException(status_code=500, detail="No messages in supervisor response")
    return response['messages'][-1]