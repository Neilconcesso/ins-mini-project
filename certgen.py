from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import datetime
import os


def save_key_and_cert(private_key, cert, key_name, cert_name):
    with open(key_name, "wb") as f:
        f.write(private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()
        ))
    with open(cert_name, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

def generate_ca_certificate():
    print("🔐 Generating CA Key Pair and Certificate...")
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CA Authority"),
        x509.NameAttribute(NameOID.COMMON_NAME, "ca.example.com"),
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        ca_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(ca_key, hashes.SHA256(), default_backend())

    save_key_and_cert(ca_key, cert, "ca_key.pem", "ca_cert.pem")
    print("✅ CA Certificate generated as ca_cert.pem")

def generate_user_certificate():
    print("🧑 Generating User Key Pair and Certificate...")
    user_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    with open("ca_key.pem", "rb") as f:
        ca_key = serialization.load_pem_private_key(f.read(), password=None)
    with open("ca_cert.pem", "rb") as f:
        ca_cert = x509.load_pem_x509_certificate(f.read())

    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "User Org"),
        x509.NameAttribute(NameOID.COMMON_NAME, "user.example.com"),
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        ca_cert.subject
    ).public_key(
        user_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(ca_key, hashes.SHA256(), default_backend())

    save_key_and_cert(user_key, cert, "user_key.pem", "user_cert.pem")
    print("✅ User Certificate generated as user_cert.pem")

def view_certificate():
    filename = input("Enter certificate filename to view (e.g., user_cert.pem): ").strip()
    try:
        with open(filename, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
            print("\n📄 Certificate Details:")
            print(cert)
    except Exception as e:
        print("❌ Error reading certificate:", str(e))

def create_fake_certificate():
    print("⚠️ Creating Fake Certificate...")
    generate_user_certificate()
    os.rename("user_cert.pem", "fake_cert.pem")
    print("🔍 Fake Certificate saved as fake_cert.pem")
