from langgraph_agent.models_anthropic import model_mix
from langgraph_agent.agent.state import State
from langgraph.types import Command
from typing import Literal
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import END
from langgraph_agent.agent.tools.memory import w_memory
tool_node = ToolNode([w_memory])
from langgraph_agent.trace import add_trace
def memorize(state:State) -> Command[Literal['tool_memo', END]]:
    with open("src/langgraph_agent/agent/SYSTEM_PROMPT/memorize.txt", 'r', encoding='utf-8') as f:
        SYSTEM_PROMPT = f.read()
    prompt = f"""
    ===== USER REQUEST =====
    {state["user_input"]}
    ===== WORK_MEMORY=====
    {state["work_memory"]}
    ===== CURRENT MEMORY =====
    {state["knowledge"]}

    Hãy quyết định có thông tin nào đáng lưu hay không.
    """
    msg = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content= prompt)
    ]
    response= model_mix(msg, [w_memory])
    print (" ===============MEMORIZE================\n"+"memorize:"+response.content+"\n")
    add_trace(" ===============MEMORIZE================\n"+"memorize:"+response.content+"\n")
    if response.tool_calls:
        next_node= 'tool_memo'
    else:
        next_node= END
    return Command(
        update={'messages': [response]},
        goto= next_node
    )
    
    