from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid

from .graph import marketing_agent_graph
from ..social_media_agent.graph import social_media_agent_graph

app = FastAPI(title="Autonomous Marketing AI Agent & Social Media Agent")

class CampaignRequest(BaseModel):
    goal: str
    platforms: List[str] = ["twitter", "linkedin"]
    budget: Optional[float] = None

class CampaignResponse(BaseModel):
    campaign_id: str
    status: str
    message: str

@app.post("/campaign/create", response_model=CampaignResponse)
async def create_campaign(request: CampaignRequest):
    """
    Trigger the creation of a new marketing campaign.
    """
    campaign_id = str(uuid.uuid4())
    
    input_state = {
        "messages": [],
        "campaign_goal": request.goal,
    }
    # In a real async scenario, we might run this in the background
    # For now, we'll just acknowledge receipt or await if we want immediate results
    # await marketing_agent_graph.ainvoke(input_state)
    
    return {
        "campaign_id": campaign_id,
        "status": "initiated",
        "message": f"Campaign creation started for goal: {request.goal}"
    }

@app.get("/campaign/{campaign_id}")
async def get_campaign_status(campaign_id: str):
    """
    Get the status of a running campaign.
    """
    return {"campaign_id": campaign_id, "status": "processing"}

class SocialPostRequest(BaseModel):
    links: List[str]
    platform: str = "twitter"

@app.post("/social/generate")
async def generate_social_post(request: SocialPostRequest):
    """
    Trigger the social media agent to generate a post.
    """
    input_state = {
        "links": request.links,
    }
    # await social_media_agent_graph.ainvoke(input_state)
    
    return {
        "status": "started",
        "message": f"Generating post for {len(request.links)} links"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
