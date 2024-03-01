table_data = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}

drinks_options = [
    {"name": "Coco-Cola", "price": 25.0},
    {"name": "Dorna", "price": 10.0},
    {"name": "Vin Alb/Rosu", "price": 40.0},
    {
        "name": "Ceai",
        "price": 20.0
    },
    {
        "name": "Cafea Americano/Espresso",
        "price": 20.0
    },
    {
        "name": "Cafea Latte",
        "price": 30.0
    },
]
salads_list = [
    {"name": "Caesar Salad", "price": 60},
    {"name": "Olivie", "price": 100},
    {"name": "Greek Salad", "price": 60},
    {"name": "Summer Salad", "price": 40},
]
soups_list = [
    {"name": "Bors Rosu", "price": 50},
    {"name": "Supa Crema", "price": 50},
    {"name": "Supa Taraneasca", "price": 50},
    {"name": "Chicken Noodle soup", "price": 50},
]
main_dishes = [
    dict(name="Cartofi Pai cu Chicken Nuggets", price=50),
    dict(name="Friptura cu Mamaliguta si branza", price=50),
]

menu = {
    'drinks': drinks_options,
    'salads': salads_list,
    'soups': soups_list,
    'main': main_dishes
}

sum_total_pe_zi = 0
toate_bucatele_din_zi = []

while True:
    print('Choose the number corresponding to your option')
    print('1. Add dish to table')
    print('2. Finish a table')
    print('Type quit to quit the program')
    main_option = input('Choose: ')
    match main_option:
        case '1':
            print('Adding a dish')
            # Meniu pentru a selecta masa
            while True:
                masa_selectata = input('Select masa, dela 1 la 10:')
                if not masa_selectata.isnumeric():
                    print('Masa nu exista')
                    continue
                masa_selectata = int(masa_selectata)
                if masa_selectata not in table_data:
                    print("Nu e corecta selectia")
                else:
                    break

            # Meniul pentru a adauga bucate
            while True:
                # Declaram meniul pentru categorii
                for category in menu:
                    print(f"Type: {category} to select the category")
                selected_category = input('\nSelect category or stop: ')
                if selected_category == 'stop':
                    break
                if selected_category.lower() not in menu:
                    print('Category not found\n')
                    continue
                list_of_elements = menu[selected_category]
                while True:
                    # Meniul pentru a selecta din categorie elemente specifice
                    print(f"\nSelect your {selected_category}")
                    for index, menu_item in enumerate(list_of_elements):
                        print(f'Type {index + 1} to select {menu_item["name"]} which costs {menu_item["price"]}')
                    selected_option = input('\nPick Option or type stop: ')
                    if selected_option == 'stop':
                        break
                    if not selected_option.isnumeric():
                        print(f"Invalid option selected, try again \n")
                        continue

                    selected_option = int(selected_option)
                    if 0 < selected_option <= len(list_of_elements):
                        dish_to_add = list_of_elements[selected_option - 1]
                        print(f'Adding item {dish_to_add} \n')
                        table_data[masa_selectata].append(dish_to_add)
                    else:
                        print('Invalid option selected \n')
        case '2':
            print('Finishing the table')
            # Checking out the table
            # Meniu pentru a selecta masa
            while True:
                masa_selectata = input('Select masa, dela 1 la 10:')
                if not masa_selectata.isnumeric():
                    print('Masa nu exista')
                    continue
                masa_selectata = int(masa_selectata)
                if masa_selectata not in table_data:
                    print("Nu e corecta selectia")
                else:
                    break

            lista_de_bucate_comandate_de_masa = table_data[masa_selectata]
            toate_bucatele_din_zi.extend(lista_de_bucate_comandate_de_masa)
            toate_bucatele = set([el['name'] for el in lista_de_bucate_comandate_de_masa])
            sum_total = 0
            for nume_bucata in toate_bucatele:
                count_this_bucata = 0
                price_this_bucata = 0
                for element in lista_de_bucate_comandate_de_masa:
                    if element['name'] == nume_bucata:
                        count_this_bucata += 1
                        price_this_bucata = element['price']
                print(
                    f"{nume_bucata} | {str(count_this_bucata).center(5)}x{str(price_this_bucata).center(6)} lei")
                print(f"Total {price_this_bucata * count_this_bucata} lei")
                sum_total += price_this_bucata * count_this_bucata
            print(f'Total total: {sum_total}')
            sum_total_pe_zi += sum_total
            table_data[masa_selectata].clear()
        case 'quit':
            can_quit = True
            for masa in table_data:
                if table_data[masa]:
                    print(f'Masa {masa} este ne finisata, nu poti inchide programul')
                    can_quit = False
            if can_quit:
                print('Goodbye')
                print(f'Total incasat azi: {sum_total_pe_zi}')
                break
        case _:
            print('Wrong choice')
