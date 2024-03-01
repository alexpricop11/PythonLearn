import json

with open("file.txt", "r") as file:
    data = json.load(file)


def all_names():
    print("List of all employee names:")
    for i, employee in enumerate(data, start=1):
        name = employee['name']
        print(f"{i}. {name}")


def list_all_positions():
    print("List all position names (without repeating the same position)")
    positions = set(employee['position'] for employee in data)
    for i, position in enumerate(positions, start=1):
        print(f"{i}. {position}")


def calculate_total_salary():
    total_salary = sum(employee['salary'] for employee in data)
    print(f"Total company salary per month: ${total_salary}")


def calculate_tax():
    try:
        tax_percentage = float(input("Enter tax percentage: "))
        tax_amount = (tax_percentage / 100) * sum(employee['salary'] for employee in data)
        print(f"Total tax per month: {tax_amount}")
    except ValueError:
        print("Please enter a valid tax percentage as a number.")


def display_top_10_highest_paid():
    sorted_data = sorted(data, key=lambda x: x['salary'], reverse=True)[:10]
    print("Top 10 highest paid employees:")
    for i, employee in sorted_data:
        print(f"Name: {employee['name']}, Position: {employee['position']}, Salary: ${employee['salary']}, "
              f"Employment Start Date: {employee['employee_from']}")


def display_top_10_longest_employment():
    sorted_data = sorted(data, key=lambda x: x['employee_from'], reverse=True)[:10]
    print("Top 10 employees with the longest time in the company:")
    for employee in sorted_data:
        print(f"Name: {employee['name']}, Position: {employee['position']}, Salary: ${employee['salary']}, "
              f"Employment Start Date: {employee['employee_from']}")


while True:
    try:
        print("MENU")
        print("0. Exit")
        print("1. List of all employee names:")
        print("2. List of all positions:")
        print("3. Calculate the amount of salary the company has to pay per month in total")
        print("4. Calculate the amount of money the company has to pay in taxes per month. "
              "(Tax % Value is input from the console)")
        print("5. Display information for the top 10 highest paid employees "
              "name, position, salary, employment_start_date) from highest paid to lower.")
        print("6. Display information for the top 10 employees with the longest time in the company "
              "(name, position, salary, employment_start_date) from highest to lower.")
        option = int(input("Select option: "))
        match option:
            case 0:
                break
            case 1:
                all_names()
            case 2:
                list_all_positions()
            case 3:
                calculate_total_salary()
            case 4:
                calculate_tax()
            case 5:
                display_top_10_highest_paid()
            case 6:
                display_top_10_longest_employment()
            case _:
                print("Enter number (1-6)")
    except ValueError:
        print("Enter valid option")
