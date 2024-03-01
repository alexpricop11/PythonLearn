def is_palindrome(text):
    rev = ''.join(reversed(text))
    if text == rev:
        return True
    return False


text_input = input("Enter a text: ")
palindrom = is_palindrome(text_input)
print(f"Palindrome: {palindrom}")