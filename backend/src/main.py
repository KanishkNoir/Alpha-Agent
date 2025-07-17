from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.db import init_db
from src.api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix = "/api/chat")

@app.get("/")
def read_index():
    return {"Hello": "World Alpha"}