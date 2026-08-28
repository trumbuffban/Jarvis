
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)
from langchain_openai import ChatOpenAI
model_1= ChatOpenAI(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["API_ATHROPIC_ROUTER"]
    )
model_2= ChatOpenAI(
    model="liquid/lfm-2.5-2.6b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["API_ATHROPIC_ROUTER"]
)
