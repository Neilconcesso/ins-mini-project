from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

def verify_certificate():
    print("🔎 Verifying user certificate with CA’s public key...")
    try:
        with open("ca_cert.pem", "rb") as f:
            ca_cert = x509.load_pem_x509_certificate(f.read())
        with open("user_cert.pem", "rb") as f:
            user_cert = x509.load_pem_x509_certificate(f.read())

        ca_cert.public_key().verify(
            user_cert.signature,
            user_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            user_cert.signature_hash_algorithm,
        )
        print("✅ Certificate is valid (signed by CA)")
    except Exception as e:
        print("❌ Certificate verification failed:", e)

def simulate_tampering():
    print("🧪 Simulating message tampering...")
    try:
        with open("signed_message.txt", "rb") as f:
            original = f.read()
        tampered = original + b"X"

        with open("signature.sig", "rb") as f:
            sig = f.read()
        with open("user_cert.pem", "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
        pub_key = cert.public_key()

        pub_key.verify(
            sig,
            tampered,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
    except Exception:
        print("🚨 Tampering detected! Signature verification failed.")
