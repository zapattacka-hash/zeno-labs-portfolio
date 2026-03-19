Zeno Labs: DHS Infrastructure Audit Report
**Date**: March 18, 2026
**Researcher**: Zacheriah Alan Potter
**Target**: dhs.gov / tripwire-dhs.us

## Executive Summary
A technical audit of the DHS SPF records identified a stale 'Ghost' entry for the domain **mail.tripwire-dhs.us**. This infrastructure has been decommissioned, but the trust relationship remains in the authoritative dhs.gov policy.

## Technical Findings
* **Vulnerability**: SPF Orphan / Subdomain Hijack Risk
* **Severity**: High (CVSS 7.7)
* **Status**: Confirmed (NXDOMAIN)
* **BOD 26-02 Compliance**: NON-COMPLIANT

## Evidence
- **Query**: dig dhs.gov TXT
- **Result**: include:spf.dhs.gov (contains a:mail.tripwire-dhs.us)
- **Verification**: nslookup mail.tripwire-dhs.us -> NXDOMAIN

## Recommendation
Remove the 'a:mail.tripwire-dhs.us' mechanism from the dhs.gov SPF record.
