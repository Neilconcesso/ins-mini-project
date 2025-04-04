import keygen
import sign
import verify

def dss_auth_system():
    """Menu-driven system for DSS authentication."""
    while True:
        print("\n=== Digital Signature System ===")
        print("1) Create DSA Key Pair")
        print("2) Sign a Text Message")
        print("3) Validate a Signature")
        print("4) Exit the Program")

        user_choice = input("Select an option (1-4): ").strip()

        if user_choice == "1":
            keygen.generate_dsa_keys()
        elif user_choice == "2":
            message = input("Enter the message to be signed: ").encode()
            sign.sign_message(message)
        elif user_choice == "3":
            message = input("Enter the original message: ").encode()
            try:
                with open("signature.sig", "rb") as sig_file:
                    signature_data = sig_file.read()
                verify.verify_signature(message, signature_data)
            except FileNotFoundError:
                print("Error: Signature file not found!")
        elif user_choice == "4":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid selection! Please choose a valid option.")

if __name__ == "__main__":
    dss_auth_system()
