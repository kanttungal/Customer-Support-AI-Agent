import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from settings import MODEL_NAME,TEMPERATURE

load_dotenv()

def get_api_key(key_name:str):
    """
    Read API key from .env(local)
    or streamlit secrets(deployment)
    """
    value = os.getenv(key_name)
    if value:
        return value
    return st.secrets[key_name]

# Read OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

# Read Tavily API Key

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# Create LLM

llm = ChatOpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = OPENROUTER_API_KEY,
    model = MODEL_NAME,
    temperature = TEMPERATURE
)


