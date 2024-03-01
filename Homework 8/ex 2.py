numar = int(input("Introduceți un număr: "))

# Verificăm utilizând bucla for
este_prim_for = True
if numar < 2:
    este_prim_for = False
else:
    for i in range(2, numar):
        if numar % i == 0:
            este_prim_for = False
            break

# Afișăm rezultatul pentru bucla for
if este_prim_for:
    print(f"{numar} este un număr prim (utilizând for).")
else:
    print(f"{numar} nu este un număr prim (utilizând for).")

# Verificăm utilizând bucla while
este_prim_while = True
if numar < 2:
    este_prim_while = False
else:
    i = 2
    while i < numar:
        if numar % i == 0:
            este_prim_while = False
            break
        i += 1

# Afișăm rezultatul pentru bucla while
if este_prim_while:
    print(f"{numar} este un număr prim (utilizând while).")
else:
    print(f"{numar} nu este un număr prim (utilizând while).")
