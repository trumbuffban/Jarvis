
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(env_path)
load_dotenv(find_dotenv())

api_key = os.getenv("API_ATHROPIC_ROUTER", "")
# Sử dụng nhiều model kiểu: model_1 fail -> model_2 fail -> model_3 -> ... để tránh tình trạng quá tải request hay limit
from langchain_openai import ChatOpenAI
lst_name_model= ["dots-studio/dots-3-note-preview:free","nvidia/nemotron-3-ultra-550b-a55b:free","liquid/lfm-2.5-2.6b:free","inclusionai/ling-3.0-flash-fin:free"]
list_model= []
for name_model in lst_name_model:
    model = ChatOpenAI(
        model=name_model,
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    list_model.append(model)

def model_mix(input_message,tools = None, schema =None):
    list_model_copy = list_model.copy()
    if tools:
        list_model_copy = [model.bind_tools(tools) for model in list_model_copy]
    if schema:
        list_model_copy= [model.with_structured_output(schema) for model in list_model_copy]
    for model in list_model_copy:
        try:
            response = model.invoke(input_message)
            return response
        except Exception as e:
            print(f"Model failed: {e}")
            continue
    raise RuntimeError("All models failed")
