from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

def verify_signature(message: bytes, signature: bytes):
    try:
        with open("certificate.pem", "rb") as cert_file:
            cert = x509.load_pem_x509_certificate(cert_file.read())
            public_key = cert.public_key()

        print(f"Verifying message: {message}")
        print(f"Signature (hex): {signature.hex()}")

        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256()
        )

        print("✔ The signature is authentic and valid!")

    except FileNotFoundError:
        print("❌ Certificate file is missing!")
    except Exception as e:
        print("❌ Signature verification failed!")
        print("Reason:", str(e))
