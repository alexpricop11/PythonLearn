from Homework15.controller.auth import authenticate_user
from Homework15.view.input_helpers import get_email_input, get_password_input


def login_view():
    email_input = get_email_input()
    attemt_limit = 3
    current_attempts = 0
    try:
        while True:
            if 0 < attemt_limit <= current_attempts:
                raise Exception("Too many attempts")
            password = get_password_input()
            result = authenticate_user(email_input, password)
            if result:
                print("Logged in successfully")
                return True
            else:
                print('Invalid password')
            current_attempts += 1
    except Exception as ex:
        print(ex)
        print('Login failed')
