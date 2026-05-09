import os
import json
import urllib.request
import urllib.error

# --- CONFIGURATION ---
# Get key from environment or paste it here (keep quotes!)
API_KEY = os.environ.get("OPENAI_API_KEY") 
MODEL = "gpt-4o"

def raw_api_call(system_prompt, user_prompt):
    """
    Talks to OpenAI without the 'openai' library.
    Uses standard Python tools only.
    """
    if not API_KEY:
        return {"error": "Missing API Key. Run: export OPENAI_API_KEY=sk-..."}

    url = "https://api.openai.com/v1/chat/completions"
    
    # The payload (JSON body)
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "response_format": {"type": "json_object"} # Enforce strict JSON
    }

    # Prepare the request
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    try:
        # Send request
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            content = result['choices'][0]['message']['content']
            return json.loads(content) # Parse the AI's JSON output
            
    except urllib.error.HTTPError as e:
        print(f"❌ API Error: {e.read().decode()}")
        return {}

# --- AGENTS ---

def orchestrator(goal):
    print(f"\n🧠 [Orchestrator] Planning: '{goal}'...")
    
    prompt = f"""
    You are a Project Manager. 
    Break the goal: '{goal}' into 3 atomic sub-tasks.
    Output strictly valid JSON: {{ "plan": ["task1", "task2", "task3"] }}
    """
    
    response = raw_api_call("You are a generic planner.", prompt)
    return response.get("plan", [])

def worker(task):
    print(f"  ⚡ [Worker] Working on: '{task}'...")
    
    prompt = f"""
    Execute this task: '{task}'. 
    Keep it brief (1 sentence).
    Output strictly valid JSON: {{ "result": "Your result here" }}
    """
    
    response = raw_api_call("You are a worker.", prompt)
    return response.get("result", "Task Failed")

# --- WORKFLOW ---

def run_workflow():
    # 1. Get the goal
    goal = "Explain how a CPU works to a 5 year old"
    
    # 2. Plan
    plan = orchestrator(goal)
    if not plan:
        print("❌ Orchestrator failed to generate a plan.")
        return

    # 3. Execute (Fan-Out)
    results = []
    for task in plan:
        output = worker(task)
        results.append(output)

    # 4. Report
    print("\n--- 🏁 FINAL REPORT 🏁 ---")
    for i, res in enumerate(results):
        print(f"{i+1}. {res}")

if __name__ == "__main__":
    run_workflow()
