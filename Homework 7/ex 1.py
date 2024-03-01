try:
    greutatea = float(input("Introduceți greutatea dumneavoastră: "))
    inaltimea = float(input("Introduceți înălțimea dumneavoastră: "))
except ValueError:
    print("Vă rugăm să introduceți valori numerice valide pentru greutate și înălțime.")
    exit()

try:
    imc = greutatea / (inaltimea ** 2)
except ZeroDivisionError:
    print("Înălțimea nu poate fi zero. Vă rugăm să introduceți o valoare nenulă pentru înălțime.")
    exit()

print(f"IMC-ul dumneavoastră este: {imc:.2f}")

if imc < 18.5:
    print("Aveți subponderal.")
elif 18.5 <= imc <= 24.9:
    print("Aveți o greutate normală.")
elif 25 <= imc <= 29.9:
    print("Aveți supraponderalitate.")
else:
    print("Aveți obezitate.")
