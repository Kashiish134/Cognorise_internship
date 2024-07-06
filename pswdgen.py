import random
import string

def generate_password(length):
    """
    Generate a password of the specified length using a combination of random characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to prompt the user for password length and generate a password.
    """
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
