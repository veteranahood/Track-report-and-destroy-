#!/bin/bash
# Description: Injects Honeytokens into hardcoded paths targeted by supply chain malware.

echo "[*] Initializing Honeytoken Deployment..."

# 1. AWS Credentials Lure
AWS_DIR="$HOME/.aws"
mkdir -p "$AWS_DIR"
if ! grep -q "AKIA_FAKE_TRACKING_TOKEN" "$AWS_DIR/credentials" 2>/dev/null; then
    cat >> "$AWS_DIR/credentials" << EOL

[production-deploy-bot]
# WARNING: DO NOT USE. MONITORED HONEYTOKEN.
aws_access_key_id = AKIA_FAKE_TRACKING_TOKEN
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCY_HONEYTOKEN
EOL
    echo "[+] Injected AWS honeytoken into $AWS_DIR/credentials"
else
    echo "[-] AWS honeytoken already exists."
fi

# 2. Git Credentials Lure
GIT_CREDS="$HOME/.git-credentials"
if ! grep -q "ghp_FakeGitHubTokenForTracking" "$GIT_CREDS" 2>/dev/null; then
    echo "https://deploy-bot:ghp_FakeGitHubTokenForTracking@github.com" >> "$GIT_CREDS"
    echo "[+] Injected GitHub honeytoken into $GIT_CREDS"
else
    echo "[-] GitHub honeytoken already exists."
fi

# 3. SSH Lure
SSH_DIR="$HOME/.ssh"
mkdir -p "$SSH_DIR"
if ! grep -q "internal-db-production" "$SSH_DIR/config" 2>/dev/null; then
    cat >> "$SSH_DIR/config" << EOL

Host internal-db-production
    HostName 10.0.0.50
    User admin
    IdentityFile ~/.ssh/id_rsa_honey
EOL
    echo "[+] Injected SSH lure into $SSH_DIR/config"
else
    echo "[-] SSH lure already exists."
fi

echo "[*] Deployment complete. Waiting for threat actor interaction."
