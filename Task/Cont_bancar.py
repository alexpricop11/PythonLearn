class ContBancar:
    def __init__(self, sold_cont):
        self.sold_cont = sold_cont

    def depune_bani(self):
        while True:
            try:
                adauga_bani = int(input("Adauga bani in cont: "))
                if adauga_bani > 0:
                    self.sold_cont += adauga_bani
                    print(f"Suma {adauga_bani} de lei a fost adaugata in cont")
                    break
                else:
                    print("Introduceti suma pozitiva")
            except ValueError:
                print("Eroare, introduceti o suma")

    def retrage_bani(self):
        while True:
            try:
                scoate_bani = int(input("Retrage bani din cont: "))
                if 0 < scoate_bani <= self.sold_cont:
                    self.sold_cont -= scoate_bani
                    print(f"A fost retrasa suma de {scoate_bani} lei")
                    break
                else:
                    print("Introdu suma care este in cont!")
            except ValueError:
                print("Introduceti suma")

    def soldul_curent(self):
        print(f"\nIn contul Dvs. este {self.sold_cont} lei")


cont = ContBancar(0)
while True:
    try:
        print("\nMENU")
        print("1. Depunere de bani in cont")
        print("2. Retragere de bani din cont")
        print("3. Verifica soldul curent a contului")
        print("4. Iesire")
        optiune = int(input("Alege o optiune: "))
        match optiune:
            case 1:
                cont.depune_bani()
            case 2:
                cont.retrage_bani()
            case 3:
                cont.soldul_curent()
            case 4:
                print("La revedere!")
                break
            case _:
                print("Introduceti o optiune din Menu")

    except ValueError:
        print("Introduceti o optiune valida")
