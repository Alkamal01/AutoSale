from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .nodes.planner import planner_node
from .nodes.executor import executor_node
from .nodes.evaluator import evaluator_node

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.add_node("evaluator", evaluator_node)

# Define edges
workflow.add_edge(START, "planner")
workflow.add_edge("planner", "executor")
workflow.add_edge("executor", "evaluator")
workflow.add_edge("evaluator", END)

# Compile
marketing_agent_graph = workflow.compile()
