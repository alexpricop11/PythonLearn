import json


def all_dish():
    try:
        with open("menu.json", "r") as file:
            dish = json.load(file)
            print(json.dumps(dish, indent=2))
    except FileNotFoundError:
        print("Fisierul nu a fost gasit")


def add_dish():
    with open('menu.json', 'r+') as file:
        try:
            data = json.load(file)

        except Exception as e:
            print(f'Eroare: {e}, fisierul json este gol sau este invalid')
            data = []
        new_dish = input("Enter a dish in menu: ").capitalize()
        data.append(new_dish)
        file.seek(0)
        json.dump(data, file, indent=2)
        print("Dish add to success")


while True:
    try:
        print("Menu")
        print("1. list all dishes")
        print("2. Adds a dish")
        print("0. Exit")
        option = int(input("Enter a option: "))
        match option:
            case 0:
                break
            case 1:
                all_dish()
            case 2:
                add_dish()
            case _:
                print("Enter a valid option")
    except ValueError:
        print("\nEnter a number")
