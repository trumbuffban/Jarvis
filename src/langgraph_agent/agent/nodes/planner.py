from langgraph_agent.models_anthropic import model_mix
from langgraph_agent.agent.state import State
from langgraph_agent.trace import add_trace
from langchain_core.messages import SystemMessage,HumanMessage
def planner(state: State):
    with open("src/langgraph_agent/agent/SYSTEM_PROMPT/planner.txt", 'r', encoding='utf-8') as f:
        SYSTEM_PROMPT= f.read()

    PROMPT = f"""

    VẤN ĐỀ NGƯỜI DÙNG:
    {state['user_input']}

    KIẾN THỨC HIỆN CÓ:
    {state['knowledge']}

    THỜI GIAN HIỆN TẠI:
    {state['current_time']}
    """
    msg = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=PROMPT)
    ]
    response = model_mix(msg)
    plan= response.content
    print (" ===============PLANNER================" + "\n" + plan + "\n")
    add_trace(" ===============PLANNER================" + "\n" + plan + "\n")

    return {
        "plan": plan,
        "messages": [response]
    }