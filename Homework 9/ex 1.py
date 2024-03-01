numere = [int(x) for x in input("Introduceți o listă de numere: ").split(',')]
produs = 1

for num in numere:
    produs *= num
    if produs > 100:
        print('Produsul este prea mare')
        break
print(f'Produsul este: {produs}')
