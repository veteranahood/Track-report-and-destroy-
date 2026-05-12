# Supply Chain Active Defense Framework

We are architecting an active-defense tracking framework to hunt threat actors exploiting open-source supply chains. By integrating deceptive honeytokens, kernel-level eBPF monitoring, and automated forensic reporting, this system shifts from passive defense to aggressive tracking, instantly identifying and escalating hacker infrastructure.

## ⚠️ CRITICAL WARNING
**Do not run this on production machines without strict isolation.** 
Recent supply chain malware (such as the Mini Shai-Hulud worm) contains a "dead-man's switch." If it detects that its stolen tokens have been revoked or manipulated, it may execute a root directory wipe (`rm -rf ~/`). Run this framework in a sandboxed or containerized environment designed for threat hunting.

## Features
1. **Honeytoken Deployment:** Automatically injects traceable, zero-permission credentials into paths frequently targeted by malware (`~/.aws/credentials`, `~/.git-credentials`, `~/.ssh/config`).
2. **eBPF Kernel Monitoring:** Uses the Extended Berkeley Packet Filter (eBPF) to monitor system calls at the kernel level, instantly detecting destructive commands like `rm -rf`.
3. **Automated Escalation:** Packages intercepted telemetry into structured incident reports for rapid analysis and escalation to cyber authorities.

## Prerequisites
* Linux environment (Ubuntu/Debian recommended for eBPF support)
* Python 3.8+
* `bcc-tools` and `python3-bcc` (for eBPF monitoring)
* Canarytokens or a zero-permission AWS IAM user for credential generation

## Installation & Setup

**Step 1: Install Dependencies**
\`\`\`bash
sudo apt-get update
sudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r) python3-bpfcc
pip install requests
\`\`\`

**Step 2: Deploy Honeytokens**
Edit `deploy_honeytokens.sh` to include your specific Canarytokens or AWS tracking keys, then run:
\`\`\`bash
chmod +x deploy_honeytokens.sh
./deploy_honeytokens.sh
\`\`\`

**Step 3: Start eBPF Monitoring**
Run the kernel monitor with root privileges to trace destructive commands:
\`\`\`bash
sudo python3 ebpf_monitor.py
\`\`\`

## Legal & Ethical Disclaimer
This framework is designed strictly for defensive threat hunting, internal network monitoring, and generating forensic telemetry. Ensure compliance with your local laws and organizational policies regarding active defense and data collection.
