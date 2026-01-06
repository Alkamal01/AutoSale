from typing import Any, Dict
from ..state import AgentState
from langchain_core.messages import SystemMessage

async def executor_node(state: AgentState) -> Dict[str, Any]:
    """
    Executor Agent: Takes the plan and executes it (generates content, posts to platforms).
    """
    plan = state.get("campaign_plan")
    if not plan:
        return {"messages": [SystemMessage(content="No plan found to execute.")]}
    
    # Mock execution
    execution_results = [
        {"platform": "Twitter", "status": "drafted", "content": "Sample tweet content"},
        {"platform": "LinkedIn", "status": "drafted", "content": "Sample LinkedIn post"}
    ]
    
    return {
        "execution_results": execution_results,
        "messages": [SystemMessage(content="Campaign execution completed.")]
    }
