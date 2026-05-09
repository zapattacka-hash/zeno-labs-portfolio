import time
import sys

def generate_rule_30(width, generations):
    print("=============================================")
    print("   🧬 ZENO-AUTOMATA: WIDE-ANGLE CHAOS")
    print("=============================================\n")
    
    state = [0] * width
    state[width // 2] = 1
    
    for _ in range(generations):
        row = "".join(["█" if cell else " " for cell in state])
        sys.stdout.write(row + "\n")
        sys.stdout.flush()
        time.sleep(0.02)
        
        next_state = [0] * width
        for i in range(1, width - 1):
            l, c, r = state[i-1], state[i], state[i+1]
            # Rule 30 logic
            next_state[i] = 1 if (l, c, r) in [(1,0,0), (0,1,1), (0,1,0), (0,0,1)] else 0
        state = next_state

generate_rule_30(width=120, generations=100)
