import random

print("=============================================")
print("   🧠 ZENO-MARKOV: PROBABILISTIC AI")
print("=============================================\n")

# Training corpus
corpus = "the hacker breached the mainframe and the system crashed. the hacker escaped the network."
words = corpus.split()

# Build the Markov transition dictionary
transitions = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

print("[*] State Machine Built. Transition logic:")
for state, next_states in transitions.items():
    print(f"    '{state}' -> {next_states}")

# Generate a new sentence
current = "the"
sentence = [current]

print("\n[+] Generating Artificial Output:\n")
for _ in range(7):
    if current in transitions:
        # Probabilistically choose the next word based on frequency
        next_word = random.choice(transitions[current])
        sentence.append(next_word)
        current = next_word
    else:
        break

print(" ".join(sentence).capitalize() + ".")
