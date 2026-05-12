#!/usr/bin/env python3
# Description: Formats and sends an automated forensic payload to a designated webhook.

import sys
import json
import requests
import datetime

# Replace with your actual SIEM, SOAR, or authority reporting webhook
WEBHOOK_URL = "https://httpbin.org/post" 

def generate_report(pid, command):
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    
    payload = {
        "incident_type": "SUSPICIOUS_SYSTEM_COMMAND",
        "severity": "CRITICAL",
        "timestamp": timestamp,
        "telemetry": {
            "process_id": pid,
            "command_executed": command,
            "trigger": "eBPF_Kernel_Monitor"
        },
        "context": "Potential dead-man's switch execution from compromised supply chain dependency."
    }
    
    print(f"[*] Formatting STIX/JSON payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code == 200:
            print("[+] Payload successfully transmitted to reporting endpoint.")
        else:
            print(f"[-] Endpoint returned status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Failed to transmit report: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 report_incident.py <PID> <COMMAND>")
        sys.exit(1)
        
    process_id = sys.argv[1]
    executed_command = sys.argv[2]
    generate_report(process_id, executed_command)
  
