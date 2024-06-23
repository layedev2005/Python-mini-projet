import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    strength = "Weak"
    if len(password) >= 8  and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
        
    elif len(password) >= 6 and (any(c.islower() for c in password) or any(c.isupper() for c in password)) and any(c.isdigit() for c in password):
        strength = "Medium"
    return strength

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    strength = check_password_strength(password)
    
    print(f"Generated Password: {password}")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
