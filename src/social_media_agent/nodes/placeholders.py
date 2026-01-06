from typing import Dict, Any
from ..state import GeneratePostState
from langchain_core.messages import SystemMessage

async def auth_socials_passthrough(state: GeneratePostState) -> Dict[str, Any]:
    return {}

async def verify_links_subgraph(state: GeneratePostState) -> Dict[str, Any]:
    # Mocking link verification
    return {"pageContents": ["Mock content from URL"], "relevantLinks": state["links"]}

async def condense_post(state: GeneratePostState) -> Dict[str, Any]:
    # Mock condensing
    return {"post": state["post"][:280], "condenseCount": state.get("condenseCount", 0) + 1}

async def schedule_post(state: GeneratePostState) -> Dict[str, Any]:
    print(f"Scheduling post: {state['post']} for {state.get('scheduleDate', 'now')}")
    return {"next": "END"}

async def rewrite_post(state: GeneratePostState) -> Dict[str, Any]:
    return {"post": "Rewritten post based on feedback"}

async def generate_content_report(state: GeneratePostState) -> Dict[str, Any]:
    return {"report": "Content is relevant and good to go."}

async def find_and_generate_images_subgraph(state: GeneratePostState) -> Dict[str, Any]:
    return {"image": {"imageUrl": "http://example.com/image.png", "mimeType": "image/png"}}

async def update_scheduled_date(state: GeneratePostState) -> Dict[str, Any]:
    return {"scheduleDate": "2025-01-01T12:00:00Z"}

async def rewrite_post_with_split_url(state: GeneratePostState) -> Dict[str, Any]:
    return {"complexPost": {"content": state["post"], "media": []}}
