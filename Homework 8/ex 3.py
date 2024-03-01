import random


numarul_corect = random.randint(1, 100)
numarul_de_incercari = 0


while True:
    ghicheste_numarul = int(input("Ghiceste numarul: "))
    numarul_de_incercari += 1
    if ghicheste_numarul == numarul_corect:
        print(f"Ai ghicit numarul numarul {numarul_corect} din {numarul_de_incercari} ori.")
    elif ghicheste_numarul > numarul_corect:
        print("Numarul este mai mic, incearca din nou")
    else:
        print("Numarul este mai mare, incearca din nou")