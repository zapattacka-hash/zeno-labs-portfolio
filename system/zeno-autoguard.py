#!/usr/bin/env python3
# Zeno-AutoGuard: CAN Bus Intrusion Detection System
# Author: Zacheriah Alan Potter (Zeno Labs)
# Description: Monitors vehicle CAN traffic for DoS and unauthorized injection.

import time
from collections import defaultdict

# Configuration
CAN_INTERFACE = 'vcan0'
DOS_THRESHOLD = 100
WHITELIST_IDS = [0x1A4, 0x2B0, 0x3C8]

class ZenoAutoGuard:
    def __init__(self):
        self.message_counts = defaultdict(int)
        self.start_time = time.time()

    def analyze_frame(self, arbitration_id, data):
        self.message_counts[arbitration_id] += 1
        current_time = time.time()

        # Check for Unauthorized IDs
        if arbitration_id not in WHITELIST_IDS:
            print(f"[!] ALERT: Unauthorized CAN ID detected -> {hex(arbitration_id)}")

        # Immediate DoS Trigger
        if self.message_counts[arbitration_id] == DOS_THRESHOLD + 1:
            print(f"[!] CRITICAL: DoS Attack Detected on ID {hex(arbitration_id)} (> {DOS_THRESHOLD} msgs)")

        # Reset counters every second to prevent memory bloat
        if current_time - self.start_time >= 1.0:
            self.message_counts.clear()
            self.start_time = current_time

# Simulated Test Execution
if __name__ == "__main__":
    print("=============================================")
    print("   🛡️ ZENO-AUTOGUARD: CAN BUS IDS ACTIVE")
    print("=============================================")

    ids = ZenoAutoGuard()

    print("[*] Monitoring network traffic...")
    ids.analyze_frame(0x1A4, b'\x00\x00\x00')
    
    # Simulating unauthorized injection
    ids.analyze_frame(0x666, b'\xFF\xFF\xFF')

    # Simulating a DoS flood
    for _ in range(105):
        ids.analyze_frame(0x2B0, b'\x01')

    print("=============================================")
    print("   [+] ANALYSIS COMPLETE")
    print("=============================================\n")
