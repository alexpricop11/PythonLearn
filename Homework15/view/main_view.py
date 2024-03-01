from Homework15.controller.auth import log_out, get_current_user
from Homework15.controller.posts import create_post, view_my_posts, view_all_posts, edit_post, delete_post
from Homework15.view.auth.login import login_view
from Homework15.view.auth.registration import register_view
from Homework15.view.input_helpers import get_strict_number_view


def run_main_menu():
    while True:
        active_user = get_current_user()
        if active_user:
            main_menu_authorized()
        else:
            main_menu_unauthorized()


def main_menu_unauthorized():
    print('1: Inregistrare')
    print('2: Autentificare')
    print('0: Iesire')
    choice = get_strict_number_view()
    match choice:
        case 0:
            exit()
        case 1:
            register_view()
        case 2:
            login_view()


def main_menu_authorized():
    print(f'Esti autentificat ca {get_current_user()}')
    print('1: Creeaza o postare')
    print('2: Vezi postarile create de mine')
    print('3: Vezi toate postarile')
    print('4: Editeaza o postare')
    print('5: Sterge o postare')
    print('0: Deconectare')
    choice = get_strict_number_view()
    match choice:
        case 0:
            log_out()
        case 1:
            create_post()
        case 2:
            view_my_posts()
        case 3:
            view_all_posts()
        case 4:
            edit_post()
        case 5:
            delete_post()


def main():
    while True:
        active_user = get_current_user()
        if active_user:
            main_menu_authorized()
        else:
            main_menu_unauthorized()
