class Contact:
    def __init__(self, nume, prenume, telefon, email):
        self.nume = nume
        self.prenume = prenume
        self.telefon = telefon
        self.email = email

    def informatii_despre_contact(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, telefon: {self.telefon}, email: {self.email}.")


class Agenda:
    lista_de_contacte = []

    def adaugare_contact_nou(self):
        nume = input("Introduceti numele: ")
        prenume = input("Introduceti prenumele: ")
        telefon = int(input("Introdu numarul: "))
        email = input("Introdceti email-ul: ")
        contact_nou = Contact(nume, prenume, telefon, email)
        self.lista_de_contacte.append(contact_nou)


    def afiseaza_toate_contactele(self):
        if not self.lista_de_contacte:
            print("Lista este goala")
        for contact in self.lista_de_contacte:
            contact.informatii_despre_contact()

    def cautare_contact_dupa_nume_familie(self):
        cautare = input("Introduceti numele sau prenumele pentru a gasi contactul: ")
        gasit = False
        for contact in self.lista_de_contacte:
            if contact.nume == cautare or contact.prenume == cautare:
                contact.informatii_despre_contact()
                gasit = True
        if not gasit:
            print("Contactul nu a fost gasit")

    def sterge_contact(self):
        print("Introduceti numele contactului pe care doriti sa-l stergeti")
        sterge = input()
        contacte_pastrate = [contact for contact in self.lista_de_contacte if contact.nume != sterge]
        if len(contacte_pastrate) == len(self.lista_de_contacte):
            print("Acest nume nu este in lista de contacte")
        else:
            self.lista_de_contacte = contacte_pastrate
            print("Contactul a fost sters")


def meniu():
    print('1. Adauga contact')
    print('2. Afiseaza toate contactele')
    print('3. Cautarea contact')
    print('4. Sterge contact')
    print('5. Iesire din aplicatie')


agenda = Agenda()
while True:
    try:
        optiune = int(input("Alege o optiune: "))
        match optiune:
            case 1:
                agenda.adaugare_contact_nou()
            case 2:
                agenda.afiseaza_toate_contactele()
            case 3:
                agenda.cautare_contact_dupa_nume_familie()
            case 4:
                agenda.sterge_contact()
            case 5:
                exit()
            case _:
                print("Introduceti o optiune valida")
    except ValueError:
        print("Introduceti un numar")