import time
import json

# --- 1. The "Blackboard" (State) ---
# In a real app, this is a database or shared memory
state = {
    "goal": "",
    "plan": [],
    "results": [],
    "status": "idle"
}

# --- 2. The Components ---

def orchestrator_agent(user_goal):
    """The Manager: Breaks goal into tasks"""
    print(f"\n🔵 [Orchestrator] Analyzing goal: '{user_goal}'...")
    time.sleep(1) # Simulating "Thinking"

    # Mocking AI output
    generated_plan = [
        {"id": 1, "task": "Research Termux API"},
        {"id": 2, "task": "Write Python Script"},
        {"id": 3, "task": "Debug Errors"}
    ]

    print(f"📋 [Orchestrator] Created Plan: {[t['task'] for t in generated_plan]}")
    return generated_plan

def worker_agent(task_info):
    """The Specialist: Executes a single task"""
    task_name = task_info['task']
    print(f"  👷 [Worker] Picked up: '{task_name}'")
    time.sleep(0.5) # Simulating work

    # Return the 'artifact'
    return f"✅ Completed: {task_name}"

def synthesizer_agent(all_results):
    """The Reporter: Merges everything"""
    print("\n🟢 [Synthesizer] All tasks done. Compiling report...")
    return "\n".join(all_results)

# --- 3. The Workflow Engine (The "Graph") ---

def run_workflow(goal):
    # Phase 1: Planning
    state["goal"] = goal
    state["plan"] = orchestrator_agent(goal)

    # Phase 2: Fan-Out (Execution)
    # In a real system, these would run in parallel threads
    print("\n--- Starting Parallel Execution ---")
    for task in state["plan"]:
        result = worker_agent(task)
        state["results"].append(result)

    # Phase 3: Reduction (Synthesis)
    final_output = synthesizer_agent(state["results"])

    print("\n--- 🏁 FINAL OUTPUT 🏁 ---")
    print(final_output)

if __name__ == "__main__":
    run_workflow("Build a Termux Agent System")
