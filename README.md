# Autonomous Marketing AI Agent

An autonomous multi-agent system engineered to plan, execute, and inspect digital marketing campaigns without constant human intervention.

This project implements a self-correcting cognitive architecture using **LangGraph**, where specialized agents collaborate to achieve high-level business goals. It moves beyond simple "chains" to a stateful, cyclic workflow capable of error recovery and iterative optimization.

## System Architecture

The core logic is decoupled into three distinct agentic roles, ensuring separation of concerns and modular scalability:

### 1. Planner Agent (Strategy)
*   **Responsibility**: Deconstructs broad user goals (e.g., "Launch Q3 efficiency campaign") into tactical steps.
*   **Logic**: Utilizes LLMs to generate valid JSON-based campaign structures, selecting appropriate platforms and budget allocations based on historical performance data.

### 2. Executor Agent (Action)
*   **Responsibility**: The side-effect handler. Interacts with external APIs (Twitter/X, LinkedIn) and databases.
*   **Logic**: Executes the Planner's step. If an API call fails, it can self-correct or request an updated plan, preventing total system failure from transient errors.

### 3. Evaluator Agent (Optimization)
*   **Responsibility**: Closes the feedback loop.
*   **Logic**: Analyzes output against the initial goal. It writes "Lessons Learned" into a Vector Memory store, allowing the system to improve its planning logic over time (e.g., learning that "Threads do better on Tuesdays").

## Technical Stack

*   **Orchestration**: [LangGraph](https://langchain-ai.github.io/langgraph/) - for building stateful, cyclic agent workflows.
*   **Memory**: Vector Database integration for semantic retrieval of past campaign performance.
*   **API**: FastAPI - providing a robust, async interface for the frontend or external triggers.
*   **Database**: PostgreSQL & SQLModel - for persistent meaningful state (campaigns, ads, users).
*   **Runtime**: Python 3.11+

## Quickstart

1.  **Environment Setup**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt  # (Ensure you generate this from pyproject.toml)
    ```

2.  **Configuration**
    Copy `.env.example` to `.env` and configure your API keys (Anthropic, OpenAI, Twitter/X, etc.).

3.  **Run the System**
    ```bash
    uvicorn src.marketing_agent.api:app --reload
    ```

4.  **Trigger a Campaign**
    ```bash
    curl -X POST http://localhost:8000/campaign/create \
         -H "Content-Type: application/json" \
         -d '{"goal": "Promote the new open-source vector DB features", "platforms": ["twitter", "linkedin"]}'
    ```

## Development

The specific agent logic can be found in `src/marketing_agent/nodes`.
*   `planner.py`: Strategy generation prompting.
*   `executor.py`: Tool definitions and API wrappers.
*   `evaluator.py`: Analysis logic and memory commits.

---
_Engineered by [Your Name]_
