from langgraph.graph import StateGraph
from langgraph_agent.agent.nodes.executor import executor, tool_node
from langgraph_agent.agent.nodes.planner import planner
from langgraph_agent.agent.nodes.evaluator import evaluation
from langgraph_agent.agent.nodes.observation import observation
from langgraph_agent.agent.nodes.memorize import memorize
from langgraph.prebuilt import ToolNode
from langgraph_agent.agent.tools.schedule import tools
from langgraph_agent.agent.tools.memory import w_memory
from langgraph.graph import END,START
from langgraph_agent.agent.state import State

builder= StateGraph(State)


builder.add_node('plan', planner)
builder.add_node('executor',executor)
builder.add_node('evaluation', evaluation)
builder.add_node('tool', tool_node)
builder.add_node('observation',observation)
builder.add_node('memorize',memorize)
tool_memo= ToolNode([w_memory])
builder.add_node('tool_memo', tool_memo)

builder.add_edge(START, 'plan')
builder.add_edge('plan','executor')
builder.add_edge('tool', 'executor')
builder.add_edge('observation', 'evaluation')
builder.add_edge('tool_memo', END)


graph= builder.compile()

