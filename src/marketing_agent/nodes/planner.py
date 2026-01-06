from typing import Any, Dict
from ..state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_openai import ChatOpenAI 

# llm = ChatOpenAI(model="gpt-4o")

async def planner_node(state: AgentState) -> Dict[str, Any]:
    """
    Planner Agent: Analyzes the goal and generates a campaign strategy.
    """
    goal = state["campaign_goal"]
    
    # In a real implementation, we would use an LLM here to generate the plan
    # response = await llm.ainvoke([
    #     SystemMessage(content="You are an expert marketing planner."),
    #     HumanMessage(content=f"Create a campaign plan for: {goal}")
    # ])
    
    # Mock plan for now
    plan = {
        "strategy": "Virality focus",
        "platforms": ["Twitter", "LinkedIn"],
        "content_ideas": ["Thread about productivity", "Link to case study"]
    }
    
    return {
        "campaign_plan": plan,
        "messages": [SystemMessage(content=f"Plan generated: {plan}")]
    }
