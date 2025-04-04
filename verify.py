from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes, serialization

def validate_signature(data: bytes, signed_data: bytes):
    """Verifies a digital signature using the stored DSA public key."""
    try:
        with open("dsa_public_key.pem", "rb") as pub_key_file:
            public_key = serialization.load_pem_public_key(pub_key_file.read())

        public_key.verify(signed_data, data, hashes.SHA256())
        print("✔ The signature is authentic and valid!")
    except FileNotFoundError:
        print("❌ Error: Public key file is missing!")
    except Exception:
        print("❌ Signature verification failed! The message or signature might be altered.")

if __name__ == "__main__":
    original_text = input("Enter the original message: ").encode()
    try:
        with open("signed_message.sig", "rb") as sig_file:
            retrieved_signature = sig_file.read()
        validate_signature(original_text, retrieved_signature)
    except FileNotFoundError:
        print("❌ Error: Signature file not found!")
