sarcine = []
while True:
    try:
        print('\nMENU')
        print('1. Adaugare sarcina noua')
        print('2. Afisare toate sarcinile')
        print('3. Stergere sarcina')
        print('4. Marcheaza sarcina ca finalizata')
        print('0. Iesiti din program')
        optiune = int(input('Alege o optiune(0-4): '))
        if optiune < 0 or optiune > 4:
            print('Alege optiunea corecta din meniu')
        match optiune:
            case 1:
                sarcina = input('Aduaga o sarcina: ')
                sarcine.append(sarcina)
                print(f'Sarcina {sarcina} a fost adaugata')
            case 2:
                if sarcine:
                    print('Sarcinile sunt:')
                    for sarcina in enumerate(sarcine, start=1):
                        print(f'{sarcina}')
                else:
                    print('Sarcine nu sunt')
            case 3:
                if sarcine:
                    sarcina_stersa = input("Alege sarcina care doresti sa o stergi: ")
                    if sarcina_stersa in sarcine:
                        sarcine.remove(sarcina_stersa)
                        print(f"Sarcina {sarcina_stersa} a fost stearsa")
                    else:
                        print('Sarcina nu exista')
                else:
                    print('Nu exista sarcini')
            case 4:
                if sarcine:
                    sarcina_marcata = input('Marcheaza sarcina care doresti sa fie finalizata: ')
                    for sarcina in sarcine:
                        if sarcina in sarcine:
                            print(f"Sarcina {sarcina_marcata} a fost marcata")
                            break
                        else:
                            print('Sarcina nu exista')
                else:
                    print('Nu exista sarcini')
            case 0:
                if sarcine:
                    print(f'Sarcinile sunt: {sarcine}')
                else:
                    print('La revedere')
                break
    except Exception:
        print('Ceva nu e in regula incearca din nou.')