sir_caractere = input("Introdu un sir de carectere: ")
num_total = len(sir_caractere)
num_vocale = 0
num_consoane = 0
for caracter in sir_caractere:
    if caracter.isalpha():
        if caracter.lower() in "aeiou":
            num_vocale += 1
        else:
            num_consoane += 1
print(f"Numarul de caractere este: {num_total}")
print(f"Numarul de vocale este: {num_vocale}")
print(f"Numarul de consoane este: {num_consoane}")