from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def create_dsa_keypair():
    """Generates a DSA key pair and saves them as PEM files."""
    priv_key = dsa.generate_private_key(key_size=2048)
    pub_key = priv_key.public_key()

    # Save the private key
    priv_pem = priv_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open("my_dsa_private.pem", "wb") as priv_file:
        priv_file.write(priv_pem)

    # Save the public key
    pub_pem = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("my_dsa_public.pem", "wb") as pub_file:
        pub_file.write(pub_pem)

    print("DSA Key Pair Successfully Created!")

if __name__ == "__main__":
    create_dsa_keypair()
s
