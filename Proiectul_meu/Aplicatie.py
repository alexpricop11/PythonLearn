import translate


def aplicatie():
    while True:
        menu = input('Alege opțiunea 1 pentru traducător sau 2 pentru calculator: ')
        if menu == '1':
            traducator()
        elif menu == '2':
            calculator()
        else:
            print("Opțiune invalidă")


def traducator():
    print("Ai ales opțiunea traducător")
    print('1. Traducere română în engleză')
    print('2. Traducere engleză în română')
    optiune = input('Alege opțiunea 1 sau 2: ')
    if optiune == '1':
        traduce('ro', 'en')
    elif optiune == '2':
        traduce('en', 'ro')
    else:
        print("Opțiune invalidă. Vă rugăm să alegeți din nou.")


def traduce(limba_aleasa, limba_tradusa):
    cuvant = input(f'Introdu cuvântul în {limba_aleasa}: ')
    translator = translate.Translator(to_lang=limba_tradusa, from_lang=limba_aleasa)
    traducere = translator.translate(cuvant)
    print(f'{cuvant} în {limba_tradusa}: {traducere}')


def calculator():
    calculare = input('Introdu exemplu de calcul: ')
    try:
        rezultat = eval(calculare)
    except Exception as e:
        print(f'Eroare la calcul {e}')
    else:
        print(f'Rezultatul este: {rezultat}')


aplicatie()
