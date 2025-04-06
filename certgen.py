from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from datetime import datetime, timedelta
import os

def generate_ca_cert():
    print("🔐 Generating CA Key Pair and Certificate...")
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CA Authority"),
        x509.NameAttribute(NameOID.COMMON_NAME, "ca.example.com"),
    ])

    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(
        issuer).public_key(public_key).serial_number(
        x509.random_serial_number()).not_valid_before(
        datetime.utcnow()).not_valid_after(
        datetime.utcnow() + timedelta(days=365)).sign(private_key, hashes.SHA256())

    with open("ca_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()))

    with open("ca_cert.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print("✅ CA Certificate generated as ca_cert.pem")
    print("\n📄 CA Certificate Details:")
    print(cert)

def generate_user_cert(filename="user_cert.pem", keyfile="user_key.pem"):
    print("🧑 Generating User Key Pair and Certificate...")
    user_private_key = ec.generate_private_key(ec.SECP256R1())
    user_public_key = user_private_key.public_key()

    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "User Org"),
        x509.NameAttribute(NameOID.COMMON_NAME, "user.example.com"),
    ])

    with open("ca_key.pem", "rb") as f:
        ca_private_key = serialization.load_pem_private_key(f.read(), password=None)
    with open("ca_cert.pem", "rb") as f:
        ca_cert = x509.load_pem_x509_certificate(f.read())

    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(
        ca_cert.subject).public_key(user_public_key).serial_number(
        x509.random_serial_number()).not_valid_before(
        datetime.utcnow()).not_valid_after(
        datetime.utcnow() + timedelta(days=365)).sign(ca_private_key, hashes.SHA256())

    with open(keyfile, "wb") as f:
        f.write(user_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()))

    with open(filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print(f"✅ User Certificate generated as {filename}")
    print("\n📄 User Certificate Details:")
    print(cert)

def create_fake_certificate():
    print("⚠️ Creating Fake Certificate...")
    generate_user_cert(filename="fake_cert.pem", keyfile="fake_key.pem")
    print("🔍 Fake Certificate saved as fake_cert.pem")
    print("\n📄 Fake Certificate Details:")
    with open("fake_cert.pem", "rb") as f:
        cert = x509.load_pem_x509_certificate(f.read())
        print(cert)

def view_certificate():
    filename = input("Enter certificate filename to view (e.g., user_cert.pem): ").strip()
    try:
        with open(filename, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
            print("\n📄 Certificate Details:")
            print(cert)
    except Exception as e:
        print(f"❌ Error reading certificate: {e}")
