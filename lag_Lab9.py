def encode(password):
    encoded = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded

def decode(password):
    decoded = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded

def main():
    encoded_password = ""

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No encoded password found. Please encode a password first.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()