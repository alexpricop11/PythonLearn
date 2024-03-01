def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number * 0.5) + 1):
        if number % i == 0:
            return False
    return True


while True:
    try:
        number_input = int(input("Enter a number: "))
        rezult = is_prime(number_input)
        if rezult:
            print("Prime number: True")
        else:
            print("Prime number: False")
        break
    except ValueError:
        print("Enter a valid number")
