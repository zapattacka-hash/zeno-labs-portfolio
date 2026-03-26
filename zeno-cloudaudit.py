 $ cat << 'EOF' > zeno-cloudaudit.py
#!/usr/bin/env python3
# Zeno-CloudAudit: Lightweight CSPM & IAM Auditor
# Author: Zacheriah Alan Potter (Zeno Labs)
# Description: Scans cloud storage buckets for public IAM exposure.

import time

# Simulated IAM Policy Responses (JSON format)
MOCK_CLOUD_BUCKETS = {
    "zeno-app-assets-prod": {"role": "roles/storage.objectViewer", "members": ["serviceAccount:backend@zeno.iam.gserviceaccount.com"]},
    "zeno-public-images": {"role": "roles/storage.objectViewer", "members": ["allUsers"]},
    "zeno-customer-backups": {"role": "roles/storage.admin", "members": ["allAuthenticatedUsers", "user:admin@zenolabs.com"]}
}

def audit_bucket(bucket_name, policy):
    """Audits a single bucket's IAM policy for public exposure."""
    print(f"[*] Auditing gs://{bucket_name} ...")
    time.sleep(0.5)

    members = policy.get("members", [])

    # Logic engine looking for open access flags
    if "allUsers" in members or "allAuthenticatedUsers" in members:
        print(f"    [!] CRITICAL: Public Access Detected in IAM Policy!")
        print(f"        -> Exposed Role: {policy.get('role')}")
        print(f"        -> Exposed Entities: {', '.join([m for m in members if 'all' in m])}")
    else:
        print("    [*] SECURE: No public IAM bindings found.")

if __name__ == "__main__":
    print("=============================================")
    print("   ☁️ ZENO-CLOUDAUDIT: CSPM IAM SCANNER")
    print("=============================================")

    for bucket, policy in MOCK_CLOUD_BUCKETS.items():
        audit_bucket(bucket, policy)
        print("-" * 45)

    print("   [+] CLOUD AUDIT COMPLETE")
    print("=============================================\n")
EOF

chmod +x zeno-cloudaudit.py
python zeno-cloudaudit.py
=============================================
   ☁️ ZENO-CLOUDAUDIT: CSPM IAM SCANNER
=============================================
[*] Auditing gs://zeno-app-assets-prod ...
    [*] SECURE: No public IAM bindings found.
---------------------------------------------
[*] Auditing gs://zeno-public-images ...
    [!] CRITICAL: Public Access Detected in IAM Policy!
        -> Exposed Role: roles/storage.objectViewer
        -> Exposed Entities: allUsers
---------------------------------------------
[*] Auditing gs://zeno-customer-backups ...
    [!] CRITICAL: Public Access Detected in IAM Policy!
        -> Exposed Role: roles/storage.admin
        -> Exposed Entities: allAuthenticatedUsers
---------------------------------------------
   [+] CLOUD AUDIT COMPLETE
=============================================
