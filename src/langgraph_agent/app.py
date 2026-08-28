
from pathlib import Path
import pandas as pd
import streamlit as st
from langgraph_agent.main import main

st.title("🤖 JARVIS")

schedule = pd.read_csv(Path(__file__).resolve().parent.parent.parent / "data" / "schedule.csv", index_col= 'date') 

st.dataframe(schedule, use_container_width=True)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Bạn muốn tôi làm gì?")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    response = main(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
