
import operator
from typing import Annotated, List, TypedDict
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from datetime import datetime
class State(TypedDict):
    #INPUT
    knowledge: str
    user_input: str
    messages: Annotated[List[str], add_messages]
    current_time: datetime
    #PLAN
    plan: List[str]
    #EXECUTION
    work_memory: Annotated[List[str],operator.add]
    last_work: List[str]
    time_call: int
    max_call: int
    #OBSERVATION / EVALUATION
    confidence: int
    feedback: Annotated[List[str], operator.add]
    retry: int
    final_output: str
    #Memorize
    last_work_memo: List[str]
    
class evaluation_model(BaseModel):
    feedback: List[str]
    confidence: float = Field(ge=0, le=1)
    approved: bool
class observation_model(BaseModel):
    work_memory: str
    final_output: str



