Digital Signature Signing
This project is a Python-based simulation of a secure ECC (Elliptic Curve Cryptography) certificate and digital signature system. It enables users to generate and manage certificates, sign and verify messages, and simulate common cryptographic attacks for educational purposes.

Features
✨ Generate CA Key Pair and Certificate

🔐 Generate User Key Pair and Certificate

✉️ Sign and Send Secure Messages

📄 View Existing Certificates

🔍 Verify Certificates

😈 Create Fake Certificate (Impersonation)

⚡ Simulate Message Tampering Attack

How It Works
The project has three main components:

certgen.py: Handles generation and management of certificates (CA and user).

sign.py: Signs messages using the user's private key.

verify.py: Verifies digital signatures and certificates. Also simulates attacks.

Installation
Clone the repository:

git clone https://github.com/Neilconcesso/ins-mini-project.git
cd ins-mini-project
Install dependencies:

pip install cryptography
Running the System
Make sure Python is installed. Then run:

python main.py
Follow the interactive menu to perform various cryptographic operations.

Menu Options
Generate CA Key Pair and Certificate
Generates the Certificate Authority's key pair and self-signed certificate.

Generate User Key Pair and Certificate
Issues a certificate signed by the CA for a user.

Sign and Send Message
Signs a message with the user's private key and stores it securely.

View Certificate
Displays the contents of existing certificates.

Verify Certificate
Verifies the authenticity of a user certificate against the CA's public key.

Create and View Fake Certificate (Impersonation)
Demonstrates a fake certificate creation for testing impersonation attacks.

Simulate Message Tampering Attack
Tamper with a signed message to demonstrate failure of signature verification.

Exit
Ends the program.


Requirements
Python 3.x

cryptography library

****
