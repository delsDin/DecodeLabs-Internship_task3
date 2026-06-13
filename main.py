import random
import string


def generate_password(length):
    """Generate a random password with letters and numbers."""
    # Define character sets: uppercase letters, lowercase letters, and digits
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits         # 0-9
    
    # Combine all characters
    all_characters = letters + digits
    
    # Generate random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


def main():
    """Main function to run the password generator."""
    print("=== RANDOM PASSWORD GENERATOR ===\n")
    
    # Ask user for password length
    while True:
        try:
            length = int(input("Enter password length (e.g., 8): "))
            if length > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"\nYour generated password: {password}")
    print("\nKeep it safe!")


if __name__ == "__main__":
    main()