from pathlib import Path
from datetime import datetime
from langchain_core.messages import HumanMessage
from langgraph_agent.agent.state import State
from langgraph_agent.agent.graph import graph

memory_path = Path(__file__).resolve().parent.parent.parent / "data" / "memory.txt"

def main(user_input: str) -> str:
    now = datetime.now()
    knowledge = ""
    with open(memory_path, "r", encoding="utf-8") as f:
            knowledge = f.read()

    initial_state = State(
        user_input=user_input,
        knowledge=knowledge,
        messages=[HumanMessage(content=user_input)],
        current_time=now,
        plan=[],
        work_memory=[],
        last_work=[],
        confidence=0,
        feedback=['chưa có feedback'],
        retry=0,
        final_output='',
        max_call=4,
        time_call=0,
        last_work_memo=[]
    )
    result = graph.invoke(initial_state)
    return result.get('final_output', '')

