def is_valid_email(email):
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False

    if "." not in domain_part:
        return False
    if len(domain_part.split(".")[-1]) < 2:
        return False
    return True


user_email = input("Enter an email address: ")
validity = is_valid_email(user_email)

print(f"Valid email address: {validity}")
