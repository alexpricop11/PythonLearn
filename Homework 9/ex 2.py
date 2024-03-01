propozitie = input("Introdu o propozitie: ")
lista_de_lungimi = [len(propozitii) for propozitii in propozitie.split()]
print(lista_de_lungimi)


sir = input("Introdu un sir: ")
litere_mari = [litera for litera in sir if litera.isupper()]
print(litere_mari)


propozitie = input("Introduceți o propoziție: ")
prima_litera = [cuvant[0] for cuvant in propozitie.split()]
print(prima_litera)
