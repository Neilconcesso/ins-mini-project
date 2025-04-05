from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_message():
    with open("user_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    message = input("Enter message to sign: ").strip().encode()

    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    with open("signed_message.txt", "wb") as f:
        f.write(message)
    with open("signature.sig", "wb") as f:
        f.write(signature)

    print("✍ Message signed successfully. Saved as signed_message.txt and signature.sig")
