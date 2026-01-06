from typing import TypedDict, Annotated, List, Optional, Any
from langgraph.graph.message import add_messages
import operator

class ImageState(TypedDict):
    imageUrl: str
    mimeType: str

class ComplexPost(TypedDict):
    content: str
    media: Optional[List[str]]

class GeneratePostState(TypedDict):
    """
    State for the Generate Post Graph.
    """
    links: List[str]
    report: Optional[str]
    
    # VerifyLinksResultAnnotation specs (flat for simplicity here, or we can nest)
    pageContents: Optional[List[str]]
    relevantLinks: Optional[List[str]]
    
    post: str
    complexPost: Optional[ComplexPost]
    scheduleDate: Optional[str] # ISO format or similar
    userResponse: Optional[str]
    
    next: Optional[str] # Route to next node
    
    image: Optional[ImageState]
    condenseCount: int 

def reduce_list(left: list, right: list) -> list:
    if right is None:
        return left
    return left + right

class GeneratePostStateAnnotated(GeneratePostState):
    # We can use Annotated for specific reducers if needed, 
    # but TypedDict doesn't support field-level annotation for reducers in standard python yet 
    # in the same way langgraph JS does with Annotation.Root.
    # In Python LangGraph, we typically use the StateGraph(State) and if we need reducers,
    # we might define them separately or use Annotated in a class-based state.
    # For now, sticking to simple TypedDict as it's the standard.
    pass
