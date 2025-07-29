import os
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME") or "gpt-4o-mini"
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")


def get_openai_llm():
    openai_params = {
        "model": OPENAI_MODEL_NAME,
        "api_key": OPENAI_API_KEY,
        "base_url": OPENAI_BASE_URL
    }

    return ChatOpenAI(**openai_params)