# password_generator.py
import random
import string

def generate_password(length, use_symbols=True, use_numbers=True):
    """
    Generate a random password.

    Parameters:
    - length (int): Length of password
    - use_symbols (bool): Include symbols if True
    - use_numbers (bool): Include numbers if True
    """
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to Password Generator!")

    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("Password should be at least 4 characters long.")
                continue

            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            password = generate_password(length, use_symbols, use_numbers)
            print(f"\n✅ Your generated password is: {password}\n")
        except ValueError:
            print("❌ Please enter a valid number.")

        choice = input("Generate another password? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye! Stay safe with strong passwords 🔒")
            break

if __name__ == "__main__":
    main()

