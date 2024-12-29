import re

def password_strength(password):
    # Initialize criteria checks
    length_check = len(password) >= 8
    uppercase_check = bool(re.search(r'[A-Z]', password))
    lowercase_check = bool(re.search(r'[a-z]', password))
    number_check = bool(re.search(r'[0-9]', password))
    special_char_check = bool(re.search(r'[@#$%^&+=]', password))

    # Assess strength
    strength = 0
    if length_check:
        strength += 1
    if uppercase_check:
        strength += 1
    if lowercase_check:
        strength += 1
    if number_check:
        strength += 1
    if special_char_check:
        strength += 1

    # Generate strength level
    if strength == 5:
        return "Strong"
    elif strength == 4:
        return "Moderate"
    elif strength == 3:
        return "Weak"
    else:
        return "Very Weak"

# Example Usage
password = input("Enter a password to assess its strength: ")
strength = password_strength(password)
print(f"Password strength: {strength}")
