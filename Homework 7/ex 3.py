timp_intrare = input("Introduceți timpul de intrare (exemplu: 11:20 PM sau 02:00): ")
perioadă = ""
try:
    if "AM" in timp_intrare or "PM" in timp_intrare:
        oră, minut_perioadă = timp_intrare.split(":")
        minut, perioadă = minut_perioadă.split()
        oră, minut = int(oră), int(minut)
        if perioadă.upper() == "PM" and oră != 12:
            oră += 12
        elif perioadă.upper() == "AM" and oră == 12:
            oră = 0
    else:
        oră, minut = map(int, timp_intrare.split(":"))
    if 0 <= oră <= 23 and 0 <= minut <= 59:
        timp_conversie = f"{oră:02d}:{minut:02d}"
        print("Timpul convertit în format de 24 de ore este:", timp_conversie)
    else:
        raise ValueError("Valori invalide pentru ore sau minute.")
except ValueError:
    print("Formatul timpului introdus nu este corect sau conține valori invalide.")