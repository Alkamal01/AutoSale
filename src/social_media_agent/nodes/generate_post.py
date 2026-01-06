from typing import Dict, Any
from ..state import GeneratePostState
# from langchain_openai import ChatOpenAI

async def generate_post(state: GeneratePostState) -> Dict[str, Any]:
    """
    Generates a post based on the report and links.
    """
    report = state.get("report", "")
    links = state.get("links", [])
    
    # Mock generation
    generated_content = f"Here is a new post based on {links}. Insights: {report}"
    
    return {"post": generated_content}
