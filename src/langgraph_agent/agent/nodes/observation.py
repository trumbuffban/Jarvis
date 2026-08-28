from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langgraph_agent.agent.state import State
from langgraph_agent.models_anthropic import model_mix
from langgraph_agent.agent.state import observation_model
from langgraph_agent.trace import add_trace
def observation(state: State):
    with open("src/langgraph_agent/agent/SYSTEM_PROMPT/observation.txt", 'r', encoding='utf-8') as f:
        SYSTEM_PROMPT = f.read()
    PROMPT= f"""
    ===== WORK MEMORY CŨ =====
    {state['work_memory']}
    ===== LAST WORK =====
    {state['last_work']}
    """
    msg = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=PROMPT)
    ]
    response = model_mix(msg, schema= observation_model)  
    print (" ===============OBVERSATION================" + "\n" + response.work_memory + "\n")
    add_trace(" ===============OBVERSATION================" + "\n" + response.work_memory + "\n")

    return {
        "last_work": [],
        "messages": [AIMessage(content=response.final_output)],
        "work_memory": [response.work_memory],
        "final_output": response.final_output,
        "time_call": 0
    }