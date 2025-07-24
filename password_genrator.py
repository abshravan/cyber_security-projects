import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character type for the password."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            password_length = int(input("Enter the desired password length (e.g., 12): "))
            if password_length <= 0:
                print("Password length must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for the length.")

    print("\nSelect character types to include (type 'yes' or 'no'):")
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    if not (include_lowercase or include_uppercase or include_digits or include_symbols):
        print("You must select at least one character type. Please try again.")
        return

    generated_password = generate_password(
        password_length,
        include_lowercase,
        include_uppercase,
        include_digits,
        include_symbols
    )

    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
