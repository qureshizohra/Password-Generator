import secrets
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def get_user_preferences():
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    return length, use_upper, use_digits, use_special

length, use_upper, use_digits, use_special = get_user_preferences()
print(generate_password(length, use_upper, use_digits, use_special))