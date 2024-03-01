cuvant1 = input("Introdu primul cuvânt: ")
cuvant2 = input("Introdu al doilea cuvânt: ")
cuvant1 = cuvant1.replace(" ", "").lower()
cuvant2 = cuvant2.replace(" ", "").lower()
try:
    if sorted(cuvant1) == sorted(cuvant2):
        print(f"{cuvant1} și {cuvant2} sunt anagrame.")
    else:
        print(f"{cuvant1} și {cuvant2} nu sunt anagrame.")
except TypeError:
    print("Introduceți cuvinte valide.")