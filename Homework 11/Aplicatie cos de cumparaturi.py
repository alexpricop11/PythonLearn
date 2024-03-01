cosul_de_cumparaturi = []
while True:
    try:
        print('\nMENIU')
        print('1. Adauga articole in cosul de cumparaturi')
        print('2. Vizualizarea cosului')
        print('3. Calcularea costului total')
        print('4. Iesire')
        optiune = int(input("Alege o optiune: "))
        match optiune:
            case 1:
                print('Adauga articole in cosul de cumparaturi!')
                id_articol = input("Introduceti ID-ul articolului: ")
                nume = input('introduceti numele articolului: ')
                cantitate = int(input('Introduceti cantitatea: '))
                pret = float(input("Introduceti pretul articolului: "))
                articol = {
                    'id': id_articol,
                    'nume': nume,
                    'cantitate': cantitate,
                    'pretul': pret
                }
                cosul_de_cumparaturi.append(articol)
                print(f'Articolul {nume} a fost adaugat in cos')
            case 2:
                if cosul_de_cumparaturi:
                    print('\nCosul de cumparaturi')
                    for articol in cosul_de_cumparaturi:
                        print(articol)
                else:
                    print("Cosul este gol")
            case 3:
                cost_total = sum(articol['cantitate'] * articol['pretul'] for articol in cosul_de_cumparaturi)
                print(f'\nCosul total al cosului: {cost_total} lei')
            case 4:
                print('Programul a fost incheiat. La revdere')
                break
            case _:
                print('Optiune invalida, va rugam sa alegeti din nou')
    except Exception:
        print('Introduceti o optiune valida')
