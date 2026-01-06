from typing import Any, Dict
from ..state import AgentState
from langchain_core.messages import SystemMessage

async def evaluator_node(state: AgentState) -> Dict[str, Any]:
    """
    Evaluator Agent: Reviews the execution results and simulated performance.
    """
    results = state.get("execution_results")
    
    # Mock evaluation
    report = "Campaign content looks aligned with the 'Virality focus' strategy."
    
    return {
        "evaluation_report": report,
        "messages": [SystemMessage(content=f"Evaluation Report: {report}")]
    }
