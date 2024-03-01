from Homework15.data.users import POSTS_DATABASE


def create_post():
    title = input("Enter the title of the post: ")
    message = input("Enter the message of the post: ")
    author = input("Enter the Author of the post: ")

    post = {"Title": title, "Message": message, "Author": author}
    POSTS_DATABASE.append(post)
    print("Post created successfully!")


def view_my_posts():
    for i, post in enumerate(POSTS_DATABASE, start=1):
        print(f"{i}: Title: {post['Title']} - Message: {post['Message']} - Author: {post['Author']}\n")


def view_all_posts():
    for i, post in enumerate(POSTS_DATABASE, start=1):
        print(f"{i}: Title: {post['Title']} - Message: {post['Message']} - Author: {post['Author']}\n")


def edit_post():
    view_my_posts()
    post_title = input("Enter the title of the post you want to edit: ")

    for post in POSTS_DATABASE:
        if post["Title"] == post_title:
            new_title = input("Enter the new title: ")
            new_message = input("Enter the new message: ")
            new_author = input("Enter the new author: ")
            post["Title"] = new_title
            post["Message"] = new_message
            post["Author"] = new_author
            print("Post edited successfully!")
            return

    print("The entered post title was not found.")


def delete_post():
    view_my_posts()
    post_title = input("Enter the title of the post you want to delete: ")

    for post in POSTS_DATABASE:
        if post["Title"] == post_title:
            POSTS_DATABASE.remove(post)
            print("Post deleted successfully!")
            return

    print("The entered post title was not found.")
