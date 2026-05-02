from encoder import ceasar_encode, base64_encode
from decoder import ceasar_decode, base64_decode

def menu():
    print("===Student Fest Encoder/Decoder===")
    print("1. Ceasar Encode")
    print("2. Ceasar Decode")
    print("3. Base64 Encode")
    print("4. Base64 Decode")
    choice = input("choose an option:")

    text = input("Enter the text:")

    if choice == "1":
        print("Encoded Text:", ceasar_encode(text))
    elif choice == "2":
        print("Decoded Text:", ceasar_decode(text))
    elif choice == "3":
        print("Encoded Text:", base64_encode(text))
    elif choice == "4":
        print("Decoded Text:", base64_decode(text))
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()