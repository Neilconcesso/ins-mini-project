from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes, serialization

def generate_signature(data: bytes):
    """Signs the provided message using the DSA private key."""
    try:
        with open("dsa_private_key.pem", "rb") as priv_key_file:
            private_key = serialization.load_pem_private_key(priv_key_file.read(), password=None)

        # Generate signature
        digital_signature = private_key.sign(data, hashes.SHA256())

        # Save signature to a file
        with open("signed_message.sig", "wb") as sig_file:
            sig_file.write(digital_signature)

        print("✔ Message has been successfully signed.")
        return digital_signature
    except FileNotFoundError:
        print("❌ Error: Private key file not found!")
    except Exception as e:
        print(f"❌ Signing failed: {e}")

if __name__ == "__main__":
    user_message = input("Enter text to be signed: ").encode()
    generate_signature(user_message)
