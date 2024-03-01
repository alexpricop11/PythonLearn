import random

while True:
    random_number = random.randint(1, 10)
    print("Generated number:", random_number)
    if random_number > 8:
        print("Generated number is greater than 8. Exiting the loop.")
        break
