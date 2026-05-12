# LEGAL & OPERATIONAL DISCLAIMER

**READ THIS CAREFULLY BEFORE CLONING, INSTALLING, OR DEPLOYING ANY CODE IN THIS REPOSITORY.**

## 1. Assumption of Risk & No Warranty
This framework ("Active Defense Tracking Framework") is provided "AS IS" and strictly for educational, research, and defensive threat-hunting purposes. The authors and contributors of this repository provide NO WARRANTY regarding its safety, efficacy, or stability. By deploying this code, you accept 100% of the risk and responsibility for any resulting damage, data loss, or system compromise.

## 2. The "Dead-Man's Switch" Warning
The threat models this framework targets (such as the "Mini Shai-Hulud" worm) are highly destructive. **Do NOT deploy this framework on production systems, personal machines, or environments containing unbacked-up data.** 
Current supply chain malware actively monitors for token revocation or manipulation. If it detects interference, it may execute catastrophic commands (e.g., `rm -rf ~/`). You must run this framework within strictly isolated, containerized, or air-gapped sandboxes designed specifically for malware detonation and analysis.

## 3. Strict Prohibition on "Hacking Back"
While this framework is designed to track threat actors and map their infrastructure, **offensive cyber operations ("hacking back") are illegal** in most jurisdictions (including under the US Computer Fraud and Abuse Act - CFAA). 
* This tool is built to gather forensic telemetry (IP addresses, user agents, C2 server locations) via deceptive honeytokens and kernel-level monitoring.
* It does **NOT** authorize, facilitate, or endorse unauthorized access to, or deletion of, attacker infrastructure. 
* "Retaliatory" actions must be limited to gathering intelligence and securely handing it over to authorized law enforcement.

## 4. Automated Reporting Compliance
The automated reporting modules (`report_incident.py`) are designed to format telemetry for rapid escalation to authorities (e.g., CISA, FBI IC3, CERTs). 
* Do not configure these scripts to spam or automatically hit public/government endpoints with unverified data. 
* Ensure your automated reporting complies with the destination agency's API guidelines and terms of service. False positives can waste valuable law enforcement resources.

## 5. Organizational Policies
Before deploying honeytokens, eBPF monitors, or automated tracking mechanisms, ensure you have explicit written authorization from your organization's IT, Security, and Legal departments. Deploying deceptive infrastructure without authorization can violate internal corporate policies.

---
**Vigilance requires discipline.** We track, we identify, and we report. We do not become the threat actors we are hunting. 
