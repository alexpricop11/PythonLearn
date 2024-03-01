import string
import random
all_letters = list(string.ascii_letters)
print(all_letters)
pass_length = int(input('Pass length: '))
password = ''
for _ in range(pass_length):
    letter_index = random.randrange(0, len(all_letters))
    password += all_letters[letter_index]
print("Parola generată:", password)