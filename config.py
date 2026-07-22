import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from settings import MODEL_NAME, TEMPERATURE

load_dotenv()

# Read OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is missing.")

# Read Tavily API Key (Optional)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# Create LLM
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    model=MODEL_NAME,
    temperature=TEMPERATURE
)
