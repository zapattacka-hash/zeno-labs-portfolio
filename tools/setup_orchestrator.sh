#!/data/data/com.termux/files/usr/bin/bash

# --- 1. Workspace Isolation ---
cd ~
echo "[*] Creating isolated workspace: ~/ai_orchestrator"
mkdir -p ~/ai_orchestrator/agents
mkdir -p ~/ai_orchestrator/auth
mkdir -p ~/ai_orchestrator/data_staging

# --- 2. System Update & Binary Injection ---
echo "[*] Installing pre-compiled binaries for Python 3.13..."
pkg update -y
pkg install -y tur-repo
pkg install -y python python-pandas python-cryptography python-grpcio python-numpy rust binutils termux-api

# --- 3. Python Library Injection ---
echo "[*] Installing Cloud SDKs..."
pip install google-cloud-firestore firebase-admin kaggle --break-system-packages

# --- 4. Worker Agent Generation ---
cat << 'INNER_EOF' > ~/ai_orchestrator/agents/worker.py
import firebase_admin
from firebase_admin import credentials, firestore
import subprocess
import os
import time

CERT_PATH = os.path.expanduser("~/ai_orchestrator/auth/service-account.json")

if not os.path.exists(CERT_PATH):
    print(f"\n[!] ERROR: Service account JSON not found at {CERT_PATH}")
    exit(1)

cred = credentials.Certificate(CERT_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()

def process_task(doc):
    data = doc.to_dict()
    task_id = doc.id
    try:
        if data.get('type') == 'SHELL':
            result = subprocess.check_output(data.get('payload'), shell=True, stderr=subprocess.STDOUT).decode()
        elif data.get('type') == 'KAGGLE_SYNC':
            dataset = data.get('payload')
            cmd = f"kaggle datasets download -d {dataset} --unzip -p ~/ai_orchestrator/data_staging"
            subprocess.run(cmd, shell=True, check=True)
            result = f"Dataset {dataset} synced."
        else:
            result = "Unknown task type"
        doc.reference.update({"status": "COMPLETED", "result": result})
    except Exception as e:
        doc.reference.update({"status": "FAILED", "error": str(e)})

def start():
    print("\n[*] Agent Active. Listening for 'PENDING' tasks...")
    query = db.collection("termux_tasks").where("status", "==", "PENDING")
    query.on_snapshot(lambda col, changes, read: [process_task(c.document) for c in changes if c.type.name == 'ADDED'])
    while True: time.sleep(1)

if __name__ == "__main__":
    start()
INNER_EOF

chmod +x ~/ai_orchestrator/agents/worker.py
termux-wake-lock
echo "[SUCCESS] Run: python ~/ai_orchestrator/agents/worker.py"
