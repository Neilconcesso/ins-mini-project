from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
import os

def verify_user_certificate():
    print("🔎 Verifying user certificate with CA’s public key...")
    try:
        with open("ca_cert.pem", "rb") as f:
            ca_cert = x509.load_pem_x509_certificate(f.read())
        with open("user_cert.pem", "rb") as f:
            user_cert = x509.load_pem_x509_certificate(f.read())

        ca_cert.public_key().verify(
            user_cert.signature,
            user_cert.tbs_certificate_bytes,
            ec.ECDSA(hashes.SHA256())
        )
        print("✅ Certificate is valid (signed by CA)")
        print("\n📄 User Certificate Details:")
        print(user_cert)
    except Exception as e:
        print(f"❌ Certificate verification failed: {e}")

def simulate_tampering():
    print("🧪 Simulating message tampering...")
    try:
        with open("signed_message.txt", "rb") as f:
            tampered_message = f.read() + b'!'
        with open("signature.sig", "rb") as f:
            signature = f.read()
        with open("user_cert.pem", "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())

        cert.public_key().verify(
            signature,
            tampered_message,
            ec.ECDSA(hashes.SHA256())
        )
        print("✅ Message is authentic and untampered.")
    except Exception:
        print("🚨 Tampering detected! Signature verification failed.")
