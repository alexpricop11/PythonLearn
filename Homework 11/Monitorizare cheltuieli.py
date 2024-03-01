"""Monitorizare cheltuieli:
Creați o aplicație de urmărire a cheltuielilor care permite utilizatorilor să-și înregistreze cheltuielile zilnice
să le clasifice și să genereze rapoarte. Utilizați dicționare pentru a stoca cheltuielile cu detalii despre dată
categorie și sumă.
Implementați funcții pentru a adăuga cheltuieli
a clasifica cheltuielile și a genera rapoarte bazate pe categorii sau date.
* Aplicația ar trebui să permită utilizatorilor să-și înregistreze cheltuielile zilnice.
* Aplicația ar trebui să clasifice cheltuielile în diferite categorii, cum ar fi alimente, transport și divertisment.
* Aplicația ar trebui să genereze rapoarte bazate pe categorii sau date.
* Aplicația ar trebui să salveze datele de cheltuieli între sesiuni."""
import json
import os

cheltuieli = {}


def incarca_datele_din_fisier():
    if os.path.exists('cheltuieli.json'):
        with open('cheltuieli.json', 'r') as file:
            try:
                cheltuieli.update(json.load(file))
                print('Datele au fost incarcate cu succes')
            except Exception as e:
                print(f'Eroare: {e}')


def adauga_cheltuieli():
    data = input('Introduceti data(anul-luna-ziua): ')
    categoria = input('Introduceti categoria unde ati cheltuie: ').capitalize()
    suma = float(input("Introduceti suma(lei): "))
    if data not in cheltuieli:
        cheltuieli[data] = []
    cheltuieli[data].append({'categoria': categoria, 'suma': suma})
    print('Cheltuiala adaugat cu succes')


def clasifica_cheltuielele():
    categorii = {}
    if not cheltuieli:
        print('Nu există nimic de clasificat')
    else:
        for cheltuieli_zilnice in cheltuieli.values():
            for cheltuiala in cheltuieli_zilnice:
                categorie = cheltuiala['categoria']
                suma = cheltuiala['suma']
                if categorie not in categorii:
                    categorii[categorie] = 0
                categorii[categorie] += suma
    return categorii


def genereaza_raport():
    optiune_raport = input('\nAlege tipul de raport (categorie/data): ')
    if optiune_raport == 'categorie':
        categorii = clasifica_cheltuielele()
        print('\nRaport după categorii:')
        for categorie, total in categorii.items():
            print(f'{categorie}, {total} lei')
    elif optiune_raport == 'data':
        data_x = input('Introduceti data de inceput (anul-luna-ziua): ')
        data_y = input('Introduceti data de sfarsit (anul-luna-ziua): ')
        print('\nRaport intre datele specificate:')
        for data, cheltuieli_zilnice in cheltuieli.items():
            if data_x <= data <= data_y:
                total_zilnic = sum(cheltuiala['suma'] for cheltuiala in cheltuieli_zilnice)
                print(f'{data}, {total_zilnic} lei')
    else:
        print('Opțiune de raport invalidă')


def salveaza_datele_de_cheltuieli():
    if cheltuieli:
        with open('cheltuieli.json', 'w') as file:
            json.dump(cheltuieli, file, indent=5)
            print('\nDatele au fost salvate cu succes!')
    else:
        print('\nNu există date de salvat.')


incarca_datele_din_fisier()

while True:
    try:
        print()
        print('1. Adaugă cheltuielele')
        print('2. Clasifica cheltuielele')
        print('3. Genereaza rapoarte')
        print('4. Salveaza datele de cheltuieli')
        print('5. Iesire')
        optiune = int(input("Alege o optiune: "))
        match optiune:
            case 1:
                adauga_cheltuieli()
            case 2:
                rezultat_clasificare = clasifica_cheltuielele()
                print('\nCheltuieli clasificate:', rezultat_clasificare)
            case 3:
                genereaza_raport()
            case 4:
                salveaza_datele_de_cheltuieli()
            case 5:
                print('\nProgramul sa incheiat. La revedere!')
                break
    except Exception as e:
        print(f'\nEroare: {e} optiune invalida, incearca din nou ')
