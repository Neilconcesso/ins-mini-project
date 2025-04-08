# Digital Signature Signing

This project is a Python-based simulation of a secure ECC (Elliptic Curve Cryptography) certificate and digital signature system. It enables users to generate and manage certificates, sign and verify messages, and simulate common cryptographic attacks for educational purposes.

## Features
✨ Generate CA Key Pair and Certificate  
🔐 Generate User Key Pair and Certificate  
✉️ Sign and Send Secure Messages  
📄 View Existing Certificates  
🔍 Verify Certificates  
😈 Create Fake Certificate (Impersonation)  
⚡ Simulate Message Tampering Attack  

## How It Works
The project has three main components:

- **certgen.py**: Handles generation and management of certificates (CA and user).
- **sign.py**: Signs messages using the user's private key.
- **verify.py**: Verifies digital signatures and certificates. Also simulates attacks.

## Installation
Clone the repository:

```bash
git clone https://github.com/Neilconcesso/ins-mini-project.git
cd ins-mini-project
