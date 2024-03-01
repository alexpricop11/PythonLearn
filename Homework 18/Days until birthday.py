from datetime import datetime


def get_days(birthday):
    now = datetime.now()
    next_birthday = datetime(now.year, birthday.month, birthday.day)
    if now > next_birthday:
        next_birthday = datetime(now.year + 1, birthday.month, birthday.day)

    days_until_birthday = (next_birthday - now).days
    return days_until_birthday


def main():
    first_name = input("Enter your name: ")
    last_name = input("Enter your surname: ")
    date_birthday = input("Enter date of birth (in the format(DD/MM/YYYY): ")
    birthday = datetime.strptime(date_birthday, "%d/%m/%Y")
    days_until_birthday = get_days(birthday)
    print(f"{first_name} {last_name} has a bithday in {days_until_birthday} days")


if __name__ == "__main__":
    main()
