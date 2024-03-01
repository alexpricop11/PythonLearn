def get_input_or_stop_view():
    optiune = input('Choose a product or write stop: ')
    if optiune.lower() == 'stop':
        return True, None
    return False, optiune


def get_strict_number_view(message="Enter a number: "):
    while True:
        try:
            print()
            value = int(input(message))
            print()
            return value
        except ValueError:
            print('Numeric value required')


def check_password_strength(password):
    if (len(password) >= 8 and
            any(a.isupper() for a in password) and
            any(b.lower() for b in password) and
            any(c.isdigit() for c in password) and
            any(c.isalpha() for c in password)
    ):
        return True
    return False


def get_email_input():
    while True:
        email_input = input('Enter your email: ')
        if is_valid_email(email_input):
            return email_input
        else:
            print('Invalid email input')


def get_password_input(check_strength=False):
    current_attempts = 0
    while True:
        password = input('Enter your password: ')
        if not check_strength:
            return password
        if check_password_strength(password):
            return password
        else:
            print('Password did not match strength criteria')
            current_attempts += 1


def is_valid_email(email):
    try:
        part_1, part_2 = email.split("@")

        if "." not in part_2 or len(part_1) < 2:
            return False

        part_2 = part_2.split(".")
        before_dot, after_dot = part_2
        if len(after_dot) >= 2 and len(before_dot) > 1:
            return True
        else:
            return False
    except Exception as e:
        return False
