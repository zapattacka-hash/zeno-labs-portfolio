from tools.sentinel_gemma_v1 import partial_trace_filter

# Simulated "Noisy" OSINT Data
noisy_data = """
[LOG] IP: 192.168.1.1 - Status: Active
[LOG] Duplicate Entry: 192.168.1.1
[LOG] Honeypot Triggered: 10.0.0.5
[ALARM] Critical vulnerability found at 172.16.254.1: SQL Injection
[LOG] Bot traffic detected from Range 192.0.2.0/24
"""

print("--- XZ Labs: Partial Trace Input ---")
print(noisy_data)

print("\n--- XZ Labs: Gemma 4 Prompt Projection ---")
result = partial_trace_filter(noisy_data)
print(result)
