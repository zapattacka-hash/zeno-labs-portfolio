import operator
from typing import List, TypedDict, Annotated
from langgraph.graph import StateGraph, END
# If 'Send' fails to import on older versions, use standard conditional edges
try:
    from langgraph.constants import Send
except ImportError:
    print("Please update langgraph: pip install -U langgraph")
    exit()

# --- CONFIGURATION ---
# Set to True to use real OpenAI/Anthropic (requires API key env var)
USE_REAL_LLM = False 

# 1. Define the State (The "Blackboard")
class State(TypedDict):
    goal: str
    plan: List[str]  # The list of sub-tasks
    results: Annotated[List[str], operator.add] # Appends worker outputs
    final_report: str

# --- MOCK LLM (Runs offline on Termux) ---
def mock_planner(goal):
    print(f"\n[LLM] Orchestrator is planning: {goal}")
    return ["Research Android APIs", "Draft Python Script", "Test in Termux"]

def mock_worker(task):
    print(f"[LLM] Worker is executing: {task}")
    return f"Done: {task}"

# --- NODES ---

def orchestrator_node(state: State):
    # In a real app, this would be: llm.with_structured_output(Plan).invoke(state['goal'])
    plan = mock_planner(state['goal'])
    return {"plan": plan}

def worker_node(state: dict):
    task = state.get("task")
    result = mock_worker(task)
    return {"results": [result]}

def synthesizer_node(state: State):
    print("\n[Synthesizer] Merging all worker results...")
    return {"final_report": "\n".join(state["results"])}

# --- LOGIC (The Fan-Out) ---

def assign_workers(state: State):
    # This is the "Fan-Out". We create a generic "worker" process 
    # for EVERY item in the 'plan' list.
    # They run in parallel (conceptually) in the graph.
    return [Send("worker", {"task": subtask}) for subtask in state["plan"]]

# --- GRAPH CONSTRUCTION ---

workflow = StateGraph(State)

# Add nodes
workflow.add_node("orchestrator", orchestrator_node)
workflow.add_node("worker", worker_node)
workflow.add_node("synthesizer", synthesizer_node)

# Set flow
workflow.set_entry_point("orchestrator")
workflow.add_conditional_edges("orchestrator", assign_workers)
workflow.add_edge("worker", "synthesizer")
workflow.add_edge("synthesizer", END)

# Compile
app = workflow.compile()

# --- EXECUTION ---

if __name__ == "__main__":
    print("--- Starting Orchestrator Worklow ---")
    initial_input = {"goal": "Build a Termux Agent"}
    
    # Run the graph
    for event in app.stream(initial_input):
        # This prints the state updates as they happen
        pass
        
    print("\n--- Workflow Complete ---")

