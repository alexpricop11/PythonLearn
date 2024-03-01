cos_cumparaturi = []


def adauga_articol(cos, id_articol, nume, cantitate, pret):
    articol = {
        'id': id_articol,
        'nume': nume,
        'cantitate': cantitate,
        'pret': pret
    }
    cos.append(articol)


def afiseaza_cos(cos):
    if cos:
        print("Cos de cumparaturi:")
        for articol in cos:
            print(f"\n{articol['nume']} "
                  f"\nCantitate: {articol['cantitate']} bucati "
                  f"\nPret: {articol['pret']} lei")
    else:
        print('Cosul este gol')


def calcularea_costului_total(cos):
    cost_total = sum(articol['cantitate'] * articol['pret'] for articol in cos)
    return cost_total


while True:
    try:
        print("\nMeniu:")
        print("1. Adauga articol")
        print("2. Afiseaza cosul")
        print("3. Calculeaza cost total")
        print("4. Iesire")

        optiune = int(input("Selectati o optiune: "))

        match optiune:
            case 1:
                id_articol = int(input("ID articol: "))
                nume = input("Nume articol: ")
                cantitate = int(input("Cantitate: "))
                pret = float(input("Pret: "))
                adauga_articol(cos_cumparaturi, id_articol, nume, cantitate, pret)
                print("Articol adaugat cu succes!")
            case 2:
                afiseaza_cos(cos_cumparaturi)
            case 3:
                cost_total = calcularea_costului_total(cos_cumparaturi)
                print(f"Cost total: {cost_total}")
            case 4:
                print("La revedere!")
                break
            case _:
                print("Optiune invalida. Incercati din nou.")
    except Exception:
        print("Introduceti o optiune valida")
