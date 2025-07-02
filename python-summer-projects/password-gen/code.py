import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_symbols=True):
    """Generate a random password with selected character types"""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    char_pool = ""

    if use_lowercase:
        char_pool += lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if not char_pool:
        return "Error: Choose at least one character type."

    password = ""
    for _ in range(length):
        password += random.choice(char_pool)

    return password

def main():
    print("🔐 Simple Password Generator 🔐")
    print("=" * 40)

    while True:
        length = input("\nEnter password length (default 12): ")
        if length == "":
            length = 12
        elif length.isdigit():
            length = int(length)
        else:
            print("Please enter a valid number.")
            continue

        if length < 4 or length > 50:
            print("Length should be between 4 and 50.")
            continue

        print("\nInclude the following character types (Y/n):")

        use_lowercase = input("Lowercase (a-z)? ").lower() != 'n'
        use_uppercase = input("Uppercase (A-Z)? ").lower() != 'n'
        use_digits    = input("Digits (0-9)? ").lower() != 'n'
        use_symbols   = input("Symbols (!@#$...)? ").lower() != 'n'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

        if password.startswith("Error"):
            print(password)
            continue

        print("\nGenerated Password:")
        print("=" * 40)
        print(password)
        print("=" * 40)

        again = input("\nGenerate another password? (Y/n): ").lower()
        if again == 'n':
            print("Goodbye! Stay secure 🔐")
            break

if __name__ == "__main__":
    main()
