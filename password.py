import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    password_length = int(input("Enter password length: "))
    include_number = input("Include number (yes/no): ").strip().lower() == 'yes'
    include_character = input("Include special characters (yes/no): ").strip().lower() == 'yes'
    
    generated_password = generate_password(password_length, include_number, include_character)
    print("Generated Password:", generated_password)