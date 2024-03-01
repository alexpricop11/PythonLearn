propozitie = input("Introduceți o propoziție: ")
lungimea = 0

for cuvant in propozitie.split():
    cuvant_mic = cuvant.lower()

    if cuvant_mic.startswith('a') or cuvant_mic.startswith('t'):
        lungimea += len(cuvant)
        continue
print(f"Lungimea totală a cuvintelor care încep cu 'A' sau 'T': {lungimea}")
