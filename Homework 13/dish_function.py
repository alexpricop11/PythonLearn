# dish_functions.py

def select_table(table_data):
    while True:
        selected_table = input('Select table (1 to 10): ')
        if not selected_table.isnumeric():
            print('Table does not exist')
            continue
        selected_table = int(selected_table)
        if selected_table not in table_data:
            print("Incorrect selection")
        else:
            return selected_table


def add_dish(table_data, menu):
    print('Adding a dish')
    masa_selectata = select_table(table_data)

    # Meniul pentru a adauga bucate
    while True:
        # Declaram meniul pentru categorii
        for category in menu:
            print(f"Type: {category} to select the category")
        selected_category = input('\nSelect category or stop: ')
        if selected_category.lower() == 'stop':
            break
        if selected_category.lower() not in menu:
            print('Category not found\n')
            continue
        list_of_elements = menu[selected_category.lower()]
        while True:
            # Meniul pentru a selecta din categorie elemente specifice
            print(f"\nSelect your {selected_category}")
            for index, menu_item in enumerate(list_of_elements, start=1):
                print(f'Type {index} to select {menu_item["name"]} which costs {menu_item["price"]}')
            selected_option = input('\nPick Option or type stop: ')
            if selected_option.lower() == 'stop':
                break
            if not selected_option.isnumeric():
                print(f"Invalid option selected, try again \n")
                continue

            selected_option = int(selected_option)
            if 0 < selected_option <= len(list_of_elements):
                dish_to_add = list_of_elements[selected_option - 1]
                print(f'Adding item {dish_to_add["name"]} \n')
                table_data[masa_selectata].append(dish_to_add)
            else:
                print('Invalid option selected \n')


def finish_table(table_data):
    print('Finishing the table')
    masa_selectata = select_table(table_data)
    toate_bucatele_din_zi = []
    lista_de_bucate_comandate_de_masa = table_data[masa_selectata]
    toate_bucatele_din_zi.extend(lista_de_bucate_comandate_de_masa)
    toate_bucatele = set([el['name'] for el in lista_de_bucate_comandate_de_masa])
    sum_total = 0
    sum_total_pe_zi = 0
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
    return sum_total


