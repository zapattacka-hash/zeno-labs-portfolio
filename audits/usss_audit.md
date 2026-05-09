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
