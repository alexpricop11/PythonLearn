with open("write_test.txt", "a") as file:
    add_text = input("Enter a text: ")
    file.write(add_text + '\n')
