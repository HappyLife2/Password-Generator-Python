# password_generator.py
import random
import string

def generate_password():
    # Characters pool
    uppercase_letters = random.choices(string.ascii_uppercase, k=2)
    lowercase_letters = random.choices(string.ascii_lowercase, k=2)
    digits = random.choices(string.digits, k=2)
    punctuation = random.choices(string.punctuation, k=2)
    
    # Combine all characters
    password_characters = uppercase_letters + lowercase_letters + digits + punctuation
    
    # Shuffle to ensure randomness
    random.shuffle(password_characters)
    
    # Join characters to form the password
    password = ''.join(password_characters)
    
    return password

if __name__ == '__main__':
    print("Generated Password:", generate_password())
