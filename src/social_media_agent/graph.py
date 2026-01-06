from langgraph.graph import StateGraph, START, END
from .state import GeneratePostState
from .nodes.generate_post import generate_post
from .nodes.human_node import human_node
from .nodes.placeholders import (
    auth_socials_passthrough, verify_links_subgraph, condense_post,
    schedule_post, rewrite_post, generate_content_report,
    find_and_generate_images_subgraph, update_scheduled_date,
    rewrite_post_with_split_url
)

def route_after_generating_report(state: GeneratePostState):
    if state.get("report"):
        return "generatePost"
    return END

def condense_or_human_conditional_edge(state: GeneratePostState):
    # Simplified logic
    post = state.get("post", "")
    if len(post) > 280 and state.get("condenseCount", 0) <= 3:
        return "condensePost"
    return "findAndGenerateImagesSubGraph"

def route_human_decision(state: GeneratePostState):
    return state.get("next", "schedulePost")

workflow = StateGraph(GeneratePostState)

workflow.add_node("authSocialsPassthrough", auth_socials_passthrough)
workflow.add_node("verifyLinksSubGraph", verify_links_subgraph)
workflow.add_node("generateContentReport", generate_content_report)
workflow.add_node("generatePost", generate_post)
workflow.add_node("condensePost", condense_post)
workflow.add_node("findAndGenerateImagesSubGraph", find_and_generate_images_subgraph)
workflow.add_node("humanNode", human_node)
workflow.add_node("schedulePost", schedule_post)
workflow.add_node("rewritePost", rewrite_post)
workflow.add_node("updateScheduleDate", update_scheduled_date)
workflow.add_node("rewriteWithSplitUrl", rewrite_post_with_split_url)

# Edges
workflow.add_edge(START, "authSocialsPassthrough")
workflow.add_edge("authSocialsPassthrough", "verifyLinksSubGraph")
workflow.add_edge("verifyLinksSubGraph", "generateContentReport") # Simplified
workflow.add_conditional_edges("generateContentReport", route_after_generating_report, ["generatePost", END])

workflow.add_conditional_edges("generatePost", condense_or_human_conditional_edge, {
    "condensePost": "condensePost",
    "findAndGenerateImagesSubGraph": "findAndGenerateImagesSubGraph"
})
workflow.add_edge("condensePost", "findAndGenerateImagesSubGraph") # simplified

workflow.add_edge("findAndGenerateImagesSubGraph", "humanNode")

workflow.add_edge("rewritePost", "humanNode")
workflow.add_edge("updateScheduleDate", "humanNode")
workflow.add_edge("rewriteWithSplitUrl", "humanNode")

workflow.add_conditional_edges("humanNode", route_human_decision, {
    "rewritePost": "rewritePost",
    "schedulePost": "schedulePost",
    "updateScheduleDate": "updateScheduleDate",
    "humanNode": "humanNode",
    "rewriteWithSplitUrl": "rewriteWithSplitUrl",
    "END": END
})

workflow.add_edge("schedulePost", END)

social_media_agent_graph = workflow.compile()
social_media_agent_graph.name = "Social Media Agent Graph"
