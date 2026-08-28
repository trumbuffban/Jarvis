from langgraph_agent.agent.state import State
from langgraph_agent.models_anthropic import model_mix
from typing import Literal
from langgraph.types import Command
from langchain_core.messages import SystemMessage, ToolMessage, HumanMessage
from langgraph_agent.agent.tools.schedule import tools 
from langgraph.prebuilt import ToolNode
from langgraph_agent.trace import add_trace
def executor(state: State) -> Command[Literal["tool", "observation"]]:
    with open("src/langgraph_agent/agent/SYSTEM_PROMPT/executor.txt", 'r', encoding='utf-8') as f:
        SYSTEM_PROMPT = f.read()
    PROMPT = f"""
    ===== SỐ LẦN GỌI TOOL TỐI ĐA=====
    {state['max_call']}
    ===== THỜI GIAN GỌI TOOL HIỆN TẠI=====
    {state['time_call']}

    ===== YÊU CẦU CỦA NGƯỜI DÙNG =====
    {state['user_input']}

    ===== KẾ HOẠCH THỰC HIỆN =====
    {state['plan']}

    ===== TIẾN TRÌNH CÔNG VIỆC, NHỮNG KẾT QUẢ ĐÃ ĐẠT ĐƯỢC =====
    {state['work_memory']}
    ===== NHỮNG CÔNG VIỆC ĐÃ THỰC HIỆN =====
    {state['last_work']}

    ===== ĐÁNH GIÁ TRƯỚC ĐÓ CỦA EVALUATOR =====
    {state['feedback'][-1]}
    ===== NHIỆM VỤ HIỆN TẠI =====
    Hãy tiếp tục thực hiện kế hoạch từ trạng thái hiện tại.
    """

    msg = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=PROMPT)
    ]

    response = model_mix(msg,tools)
    last_work= state['last_work'].copy()
    if isinstance(state['messages'][-1], ToolMessage):
        last_work.append(state['messages'][-1])
    last_work.append(response)
    if response.tool_calls and state['time_call'] <= state['max_call']:
        time_call = state['time_call']+1
        next_node = "tool"
        for tool in response.tool_calls:
            print (" ===============EXECUTOR================\n"+"thực hiện: " + tool["name"] + "\n")
            add_trace(" ===============EXECUTOR================\n"+"thực hiện: " + tool["name"] + "\n")
    else:
        next_node = "observation"
        time_call = state['time_call']
        print (" ===============EXECUTOR================\n"+"kết quả: " + response.content + "\n")
        add_trace(" ===============EXECUTOR================\n"+"kết quả: " + response.content + "\n")
    return Command(
        update={
            "messages": [response],
            "last_work": last_work,
            "time_call": time_call
        },
        goto=next_node
    )
tool_node = ToolNode(tools)