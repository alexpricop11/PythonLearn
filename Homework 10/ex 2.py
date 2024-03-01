eveniment1 = [input("Introduceți participanții la primul eveniment: ")]
eveniment2 = [input("Introduceți participanții la al doilea eveniment: ")]
eveniment3 = [input("Introduceți participanții la al treilea eveniment: ")]
set_eveniment1 = set(eveniment1)
set_eveniment2 = set(eveniment2)
set_eveniment3 = set(eveniment3)
participanti_la_toate = set_eveniment1.intersection(set_eveniment2, set_eveniment3)
doar_primul_eveniment = set_eveniment1.difference(set_eveniment2, set_eveniment3)
doar_al_doilea_eveniment = set_eveniment2.difference(set_eveniment1, set_eveniment3)
primul_si_al_treilea_eveniment = set_eveniment1.intersection(set_eveniment3)
print(f"Participanții care au participat la toate cele trei evenimente: {participanti_la_toate}")
print(f"Participanții care au participat doar la primul eveniment: {doar_primul_eveniment}")
print(f"Participanții care au participat doar la al doilea eveniment: {doar_al_doilea_eveniment}")
print(f"Participanții de la primul eveniment care au participat și la al treilea eveniment: {primul_si_al_treilea_eveniment}")