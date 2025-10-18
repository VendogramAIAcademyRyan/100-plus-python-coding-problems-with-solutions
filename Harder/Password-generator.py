from random import *
from string import *
def generate_password_with_input(length, use_uppercase, use_numbers, use_special):
    input_characters = input("Enter characters to include in the password: ")
    lowercase_chars =  choice(input_characters) if input_characters else ''
    uppercase_chars = choice(input_characters) if use_uppercase else ''
    number_chars = choice(input_characters) if use_numbers else ''
    special_chars = choice(input_characters) if use_special else ''
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    if len(all_chars) < length:
        all_chars += ''.join(choice(input_characters) for _ in range(length - len(all_chars)))
    password = ''.join(sample(all_chars, length))
    return password
length = int(input("Enter desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'
password = generate_password_with_input(length, use_uppercase, use_numbers, use_special)
print("Generated Password:", password)
