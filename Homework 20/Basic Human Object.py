from datetime import date, datetime


class Human:
    def __init__(self, first_name, last_name, date_of_brith):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_brith = date_of_brith

    def get_fullname(self):
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        self.first_name = first_name
        self.last_name = last_name

    def get_age(self):
        date_of_birth_str = input("Enter date of birth (in the format DD/MM/YYYY): ")
        self.date_of_brith = datetime.strptime(date_of_birth_str, "%d/%m/%Y").date()
        today = date.today()
        brithday = today.year - self.date_of_brith.year - (
                (today.month, today.day) < (self.date_of_brith.month, self.date_of_brith.day))
        self.date_of_brith = brithday


if __name__ == "__main__":
    human = Human(first_name='', last_name='', date_of_brith='')
    human.get_fullname()
    human.get_age()
    print(f"{human.first_name} {human.last_name} {human.date_of_brith} years old")
