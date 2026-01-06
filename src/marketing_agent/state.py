from typing import TypedDict, Annotated, List, Optional, Any
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """
    State for the Autonomous Marketing Agent.
    """
    messages: Annotated[List[BaseMessage], add_messages]
    campaign_goal: str
    campaign_plan: Optional[dict]
    execution_results: Optional[List[dict]]
    evaluation_report: Optional[str]
    memory_context: Optional[List[dict]]
    user_feedback: Optional[str]
