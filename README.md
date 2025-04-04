This project implements a Digital Signature System (DSS) using DSA (Digital Signature Algorithm) to securely sign and verify messages.

1️⃣ keygen.py generates a private-public key pair and saves them in PEM format.
2️⃣ sign.py loads the private key and signs a given message using SHA-256 hashing.
3️⃣ verify.py loads the public key and verifies the message’s signature to check authenticity.
4️⃣ main.py provides a CLI menu for generating keys, signing messages, and verifying signatures.
5️⃣ Private keys are stored in dsa_private_key.pem, public keys in dsa_public_key.pem, and signatures in signature.sig.
6️⃣ The signature ensures integrity—if the message changes, verification fails.









