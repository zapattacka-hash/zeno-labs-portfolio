 Zeno Labs: TSA Infrastructure Audit
**Date**: March 18, 2026
**Researcher**: Zacheriah Alan Potter
**Target**: tsa.gov / *.tsa.gov

## Executive Summary
A technical reconnaissance audit was conducted on the Transportation Security Administration (TSA) external perimeter. The audit verified a highly hardened security posture, confir~ $ cat << 'EOF' > usss_audit.md             # Zeno Labs: USSS Infrastructure Audit
**Date**: March 18, 2026
**Researcher**: Zacheriah Alan Potter
**Target**: secretservice.gov / *.secretservice.gov                                                                                    ## Executive Summary
A technical reconnaissance audit of the United States Secret Service (USSS) external perimeter identified a hardened multi-cloud architecture. While email and web application perimeters enforce strict access controls, a global Information Disclosure vulnerability was identified on the primary CDN edge.

## Technical Findings
* **Vulnerability**: Information Disclosure (Akamai Pragma Debug Header Leak)             * **Severity**: Low (Reconnaissance Aid)
* **Status**: Confirmed globally across Akamai-routed endpoints.

## Evidence
- **Query**: `curl -Is https://www.secretservice.gov`
- **Result**: `server-timing: ak_p; desc="[REDACTED_ROUTING_METRICS]";dur=1`
- **Impact**: Exposes internal CDN routing times, cache hierarchy, and edge node performance metrics to the public internet, which can be leveraged to map network topologies.

## Infrastructure Highlights
* **Mail Trust Policy**: Fully isolated Microsoft 365 environment (`spf.protection.outlook.com`). Zero inherited vulnerabilities from DHS root domains.
* **Cloud Architecture**: Verified strict usage of `Microsoft-Azure-Application-Gateway/v2` protecting sensitive internal subdomains (e.g., `stars.secretservice.gov`).
EOF
~ $ git add tsa_audit.md usss_audit.md
git commit -m "Add TSA and USSS infrastructure audit reports"
git push origin main
fatal: not a git repository (or any parent up to mount point /data/data)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /data/data)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /data/data)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
~ $ cat usss_audit.md
# Zeno Labs: USSS Infrastructure Audit
**Date**: March 18, 2026
**Researcher**: Zacheriah Alan Potter
**Target**: secretservice.gov / *.secretservice.gov

## Executive Summary
A technical reconnaissance audit of the United States Secret Service (USSS) external perimeter identified a hardened multi-cloud architecture. While email and web application perimeters enforce strict access controls, a global Information Disclosure vulnerability was identified on the primary CDN edge.

## Technical Findings
* **Vulnerability**: Information Disclosure (Akamai Pragma Debug Header Leak)
* **Severity**: Low (Reconnaissance Aid)
* **Status**: Confirmed globally across Akamai-routed endpoints.

## Evidence
- **Query**: `curl -Is https://www.secretservice.gov`
- **Result**: `server-timing: ak_p; desc="[REDACTED_ROUTING_METRICS]";dur=1`
- **Impact**: Exposes internal CDN routing times, cache hierarchy, and edge node performance metrics to the public internet, which can be leveraged to map network topologies.

## Infrastructure Highlights
* **Mail Trust Policy**: Fully isolated Microsoft 365 environment (`spf.protection.outlook.com`). Zero inherited vulnerabilities from DHS root domains.
* **Cloud Architecture**: Verified strict usage of `Microsoft-Azure-Application-Gateway/v2` protecting sensitive internal subdomains (e.g., `stars.secretservice.gov`).
