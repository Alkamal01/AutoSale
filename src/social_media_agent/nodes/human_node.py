from typing import Dict, Any
from ..state import GeneratePostState
from langgraph.types import interrupt

async def human_node(state: GeneratePostState) -> Dict[str, Any]:
    """
    Node that pauses execution to wait for user input.
    """
    user_input = interrupt("Please approve or reject the post.")
    
    # Logic to interpret user input would go here
    # For now, we assume simple strings or a structured dict from the frontend
    
    if isinstance(user_input, dict) and user_input.get("action") == "approve":
        return {"next": "schedulePost"}
    
    elif isinstance(user_input, dict) and user_input.get("action") == "rewrite":
        return {"userResponse": user_input.get("feedback"), "next": "rewritePost"}
        
    return {"next": "schedulePost"} # Default to schedule for now
