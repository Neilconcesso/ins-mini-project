# ECC Certificate & Messaging System
Overview
The ECC Certificate & Messaging System is a secure communication application that leverages Elliptic Curve Cryptography (ECC) to manage digital certificates and secure messaging. This system allows users to generate key pairs, create and verify certificates, sign messages, and simulate various security scenarios.

# Features
Generate CA Key Pair and Certificate: Create a Certificate Authority (CA) key pair and self-signed certificate.
Generate User Key Pair and Certificate: Generate a user-specific key pair and certificate signed by the CA.
Sign and Send Message: Sign a message with the user's private key and send it securely.
View Certificate: Display the details of a generated certificate.
Verify Certificate: Check the validity of a certificate against the CA's public key.
Create and View Fake Certificate: Simulate the creation of a fake certificate for educational purposes.
Simulate Message Tampering Attack: Demonstrate how message integrity can be compromised.
Exit: Safely exit the application.
# Requirements
Python 3.x
Required libraries:
cryptography
pycryptodome
You can install the required libraries using pip:

```bash
Run
Copy code
pip install cryptography pycryptodome
```
Installation
Clone the repository:

```bash
Run
Copy code
git clone https://github.com/yourusername/ecc-certificate-messaging-system.git
cd ecc-certificate-messaging-system
```
Ensure you have the required libraries installed as mentioned above.

Usage
Run the program:

```bash
Run
Copy code
python main.py
```

Follow the on-screen prompts to use the various features of the system.

# Example Workflow
Generate a CA key pair and certificate.
Generate a user key pair and certificate signed by the CA.
Sign a message and send it.
View the generated certificate.
Verify the certificate's authenticity.
Create a fake certificate and view its details.
Simulate a message tampering attack to see how it affects message integrity.
Exit the application.
Code Structure
certgen.py: Contains functions for generating certificates and viewing them.
sign.py: Contains functions for signing messages and sending them.
verify.py: Contains functions for verifying certificates and simulating tampering.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

# Acknowledgments
Elliptic Curve Cryptography
Cryptography Library Documentation
