from dish_function import add_dish, finish_table
from table_data import initialize_tables
from menu_func import menu


sum_total_pe_zi = 0
table_data = initialize_tables()

while True:
    print('Choose the number corresponding to your option')
    print('1. Add dish to table')
    print('2. Finish a table')
    print('Type quit to quit the program')
    main_option = input('Choose: ')
    match main_option:
        case '1':
            add_dish(table_data, menu)
        case '2':
            sum_total_pe_zi += finish_table(table_data)  # Update total for the day
        case 'quit':
            can_quit = True
            for table in table_data:
                if table_data[table]:
                    sum_total_pe_zi = finish_table(table_data[table])  # Update total for the day
                    print(f'Table {table} is not checked out, can not quit.')
                    can_quit = False
            if can_quit:
                print('Goodbye')
                print(f'Total incasat azi: {sum_total_pe_zi}')
                break
        case _:
            print('Wrong choice')
