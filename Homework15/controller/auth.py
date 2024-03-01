from Homework15.data.users import USERS_DATABASE

current_user = None
is_admin = False

ADMIN_EMAIL = 'admin@admin.local'
ADMIN_PASSWORD = '123'


class RegistrationError(Exception):
    pass


class LoginError(Exception):
    pass


def authenticate_user(email, password):
    global current_user
    global is_admin
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        current_user = email
        is_admin = True
        return True

    for user in USERS_DATABASE:
        if user['email'] == email:
            if user['password'] != password:
                raise LoginError('Incorrect password')
            current_user = email
            return True

    raise LoginError("Incorrect email")


def register_user(email, password):
    all_registered_emails = [a['email'] for a in USERS_DATABASE]
    if email in all_registered_emails:
        raise RegistrationError('Email already registered')
    USERS_DATABASE.append({'email': email, 'password': password})
    return True


def log_out():
    global current_user
    global is_admin
    current_user = None
    is_admin = False


def get_current_user():
    return current_user


def get_is_admin():
    return is_admin


def get_all_users():
    return USERS_DATABASE
