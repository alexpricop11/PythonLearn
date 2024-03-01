def check_password_strength(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    special_characters = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            return True

    return has_upper and has_lower and has_digit


password_input = input("Enter a password: ")
strength = check_password_strength(password_input)

print(f"Password strength: {strength} (meets the criteria)" if strength else "Password strength: False (does not meet "
                                                                             "the criteria)")
