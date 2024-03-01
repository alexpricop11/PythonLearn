class Car:
    def __init__(self, marca, an_fabricatie, culoare, viteza_curenta):
        self.marca = marca
        self.an_fabricatie = an_fabricatie
        self.culoare = culoare
        self.viteza_curenta = viteza_curenta

    def acceleration(self):
        viteza = int(input("Introduceti viteza masinii (km/h): "))
        self.viteza_curenta = viteza

    def breakers(self):
        while True:
            viteza = int(input("Introduceti viteza masinii dupa ce a franat: "))
            if viteza < self.viteza_curenta:
                self.viteza_curenta = viteza
                break
            else:
                print(f'Nu poti sa introduci viteza dupa franare mai mare ca viteza curenta care este '
                      f'{self.viteza_curenta}')

    def stop(self):
        self.viteza_curenta = 0

    def mark(self):
        marca = input("Introduceti marca masinii: ")
        self.marca = marca

    def fabrication_year(self):
        anul = int(input("Introduceti anul fabricarii: "))
        self.an_fabricatie = anul

    def color(self):
        culoare = input("Introduceti culoarea masinii: ")
        self.culoare = culoare


car = Car(marca="", an_fabricatie=0, culoare="", viteza_curenta=0)

car.mark()
car.fabrication_year()
car.color()

car.acceleration()
print(f"Masina de marca {car.marca}, anul fabricatiei {car.an_fabricatie}, culoarea {car.culoare} care a accelerat"
      f" pana la viteza de {car.viteza_curenta} km/h")

car.breakers()
print(f"Dupa franare, masina are viteza de {car.viteza_curenta} km/h")

car.stop()
print(f"Masina de marca {car.marca}, anul fabricatiei {car.an_fabricatie}, culoarea {car.culoare} a fost oprita"
      f" cu viteza {car.viteza_curenta} km/h")
