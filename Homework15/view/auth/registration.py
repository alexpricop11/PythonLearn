from Homework15.controller.auth import register_user, RegistrationError
from Homework15.view.input_helpers import get_email_input, get_password_input


def register_view():
    email_input = get_email_input()
    password = get_password_input(True)
    try:
        register_user(email_input, password)
        print('Registration successful')
        return True
    except RegistrationError as ex:
        print(f"Registration Failed: {ex}")
        return False
