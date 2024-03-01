try:
    numere = input("Introduceți o listă de numere separate prin virgulă: ")
    numbers = [int(num) for num in numere.split(',')]
except ValueError:
    print("Vă rugăm să introduceți numere valide.")
    exit()

numere_pare = sum(num for num in numbers if num % 2 == 0)
numere_impare = sum(num for num in numbers if num % 2 != 0)

print(f"Suma numerelor pare: {numere_pare}")
print(f"Suma numerelor impare: {numere_impare}")
print(f"Lista de numere: {numbers}")
