import certgen
import sign
import verify

def dss_auth_system():
    while True:
        print("\n📜 ECC Certificate & Messaging System")
        print("1. Generate CA Key Pair and Certificate")
        print("2. Generate User Key Pair and Certificate")
        print("3. Sign and Send Message")
        print("4. View Certificate")
        print("5. Verify Certificate")
        print("6. Create and View Fake Certificate (Impersonation)")
        print("7. Simulate Message Tampering Attack")
        print("8. Exit")
        choice = input("➡ Select an option (1-8): ").strip()

        if choice == "1":
            certgen.generate_ca_cert()
        elif choice == "2":
            certgen.generate_user_cert()
        elif choice == "3":
            sign.sign_and_send_message()
        elif choice == "4":
            certgen.view_certificate()
        elif choice == "5":
            verify.verify_user_certificate()
        elif choice == "6":
            certgen.create_fake_certificate()
        elif choice == "7":
            verify.simulate_tampering()
        elif choice == "8":
            print("👋 Exiting... Have a secure day!")
            break
        else:
            print("❌ Invalid selection!")

if __name__ == "__main__":
    dss_auth_system()
