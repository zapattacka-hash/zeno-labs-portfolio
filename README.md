# Zeno Labs
**Principal Security Researcher**: Zacheriah Alan Potter

## Mission
Zeno Labs specializes in high-impact security audits, infrastructure reconnaissance, and federal compliance validations (Zero Trust, CISA Directives). 

## Core Competencies
* **Reconnaissance & OSINT**: Advanced DNS mapping, Origin IP discovery, and perimeter profiling.
* **Infrastructure Auditing**: Cloud firewall (WAF) analysis, CDN unmasking (Akamai/Cloudflare), and legacy asset identification.
* **Vulnerability Assessment**: Subdomain takeover mitigation, SPF/DMARC analysis, and compliance verification (e.g., CISA BOD 26-02).
* **Tooling**: Mobile-first auditing via Termux, Nmap, OpenSSL, and advanced Bash scripting.

## Featured Audits
* **[March 2026] Department of Homeland Security (DHS) Infrastructure Audit**
  * **Focus**: Perimeter mapping and DNS integrity.
  * **Finding**: Identified a critical SPF orphaned record (Subdomain Hijack Risk) linked to legacy counter-terrorism infrastructure. 
  * **Impact**: Prevented high-authority federal domain spoofing.
  * **Link**: [View the DHS Audit Report](dhs_audit.md)

## Rules of Engagement
All security research is conducted passively and strictly within authorized Vulnerability Disclosure Programs (VDP). Zeno Labs adheres to a strict "Identify and Report" methodology without active exploitation.


---

# Zeno Labs Custom Tooling

## Zeno-Scanner: Edge Compliance & Recon Automation
**Developer**: Zacheriah Alan Potter (Zeno Labs)
**Version**: 1.0.0

### Overview
Zeno-Scanner is a lightweight, automated Bash utility designed to fingerprint edge infrastructure, resolve origin IPs, and extract critical email trust policies (SPF/DMARC). It streamlines the initial reconnaissance phase of external perimeter audits.

### Usage
`./zeno-scanner.sh <target-domain>`

---

## Zeno-Phantom: Dangling CNAME & Takeover Scanner
**Developer**: Zacheriah Alan Potter (Zeno Labs)
**Version**: 1.0.0

### Overview
Zeno-Phantom is an automated exploitation-hunting script designed to detect Subdomain Takeover vulnerabilities. It parses lists of target subdomains, resolves their CNAME records, and cross-references them against known hijackable cloud infrastructure providers (Azure, AWS, GitHub Pages, etc.).

### Usage
`./zeno-phantom.sh <subdomains-list.txt>`

---

## Zeno-CloudAudit: CSPM & IAM Policy Scanner
**Developer**: Zacheriah Alan Potter (Zeno Labs)
**Version**: 1.0.0
**Language**: Python 3

### Overview
Zeno-CloudAudit is a lightweight Cloud Security Posture Management (CSPM) utility. Misconfigured cloud storage is a primary vector for modern data breaches. This tool automates the auditing process by parsing Identity and Access Management (IAM) JSON policies to detect unintentionally exposed assets.

### Features
* **IAM Policy Parsing**: Iterates through cloud storage bucket configurations to evaluate permission bindings.
* **Public Exposure Detection**: Automatically flags critical misconfigurations where `allUsers` or `allAuthenticatedUsers` are granted read/write or admin roles.
* **Rapid Triage**: Outputs clear, actionable alerts identifying the exact exposed role and bucket, allowing security teams to immediately revoke public access.

### Usage
`python3 zeno-cloudaudit.py`

## 🔍 Zeno-Dorker: Automated OSINT Payload Generator
**Developer:** Zacheriah Alan Potter | Zeno Labs
**Language:** Python 3
**Category:** Open-Source Intelligence (OSINT) / Reconnaissance

### Overview
`Zeno-Dorker` is a lightweight, automated reconnaissance engine designed to bypass search engine anti-bot mechanisms (like CAPTCHA blacklists). It dynamically generates URL-encoded Google Dork payloads to identify exposed infrastructure, leaked documents, and misconfigured access portals across any specified target domain. 

### Threat Vectors Targeted
* **Exposed Government/Corporate Documents:** Automates the discovery of improperly secured `.pdf` and `.xlsx` files containing sensitive classifications (e.g., FOUO, CUI, Confidential).
* **Leaked Server Logs & Databases:** Hunts for exposed `.log`, `.sql`, and `.env` files that inadvertently broadcast system architecture or credentials.
* **Hidden Admin Directories:** Maps undocumented web server structures by targeting `inurl:admin`, `login`, and `intranet` endpoints.
* **Employee PII & Access Rosters:** Scours domains for internal spreadsheets (`.xls`, `.csv`) indicating employee matrices, clearance levels, or active network rosters.

### Usage
```bash
python3 zeno-dorker.py [target-domain.com]


