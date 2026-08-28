
from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from langgraph_agent.agent.state import State
# pyrefly: ignore [missing-import]
from langgraph.graph import END
from langgraph_agent.models_anthropic import model_mix
from langgraph_agent.agent.state import evaluation_model
from typing import Literal
from langgraph.types import Command
from langchain_core.messages import SystemMessage
from langgraph_agent.trace import add_trace
def evaluation(state: State) -> Command[Literal["executor", "memorize"]]:
    with open("src/langgraph_agent/agent/SYSTEM_PROMPT/evaluator.txt", 'r', encoding='utf-8') as f:
        SYSTEM_PROMPT = f.read()
    PROMPT = f"""   

    ===== USER PROBLEM =====
    {state['user_input']}

    ===== PLAN =====
    {state['plan']}

    ===== WORK MEMORY =====
    {state['work_memory']}

    ===== CURRENT OUTPUT =====
    {state["final_output"]}

    ===== PREVIOUS FEEDBACK =====
    {state['feedback']}

    Hãy đánh giá CURRENT OUTPUT.
    """
    msg = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=PROMPT)
    ]

    response = model_mix(msg, schema=evaluation_model)
    retry = state['retry']
    
    if response.approved and response.confidence >= 0.8:
        next_node = "memorize"
    elif retry ==5:
        next_node = END
    else:
        next_node = "executor"
        retry +=1
    add_trace(" ===============EVALUATION================\n"+"feedback:"+f"{response.feedback}"+"\n")
    print (" ===============EVALUATION================\n"+"feedback:"+f"{response.feedback}"+"\n")

    return Command(
        update={
            "feedback": response.feedback,
            "confidence": response.confidence,
            "retry": retry,
            "messages": [AIMessage(content= response.feedback)] 
        },
        goto=next_node
    )
    