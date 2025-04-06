from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
import os

def sign_and_send_message():
    message = input("Enter message to sign: ").encode()
    try:
        with open("user_key.pem", "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

        with open("signed_message.txt", "wb") as f:
            f.write(message)
        with open("signature.sig", "wb") as f:
            f.write(signature)

        print("✍ Message signed successfully. Saved as signed_message.txt and signature.sig")
    except Exception as e:
        print(f"❌ Signing failed: {e}")
