from datetime import datetime, timedelta
import time


def get_event_date():
    while True:
        date_str = input("Enter the date and time (dd/mm/YYYY HH:MM): ")
        try:
            event_date = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
            one_year_from_now = datetime.now() + timedelta(days=365)

            if datetime.now() < event_date <= one_year_from_now:
                return event_date
            else:
                print("Error: Please enter a valid date and time within the next year.")
        except ValueError:
            print("Error: Please enter the date and time in the correct format.")


def get_event_name():
    return input("Enter the event name: ")


def countdown_timer(event_date, event_name):
    while datetime.now() < event_date:
        time_remaining = event_date - datetime.now()
        remaining_str = (f"{time_remaining.days} days {time_remaining.seconds // 3600} hours "
                         f"{((time_remaining.seconds // 60) % 60)} minutes "
                         f"{time_remaining.seconds % 60} seconds left until {event_name}")
        print(remaining_str)
        time.sleep(1)

    print(f"\n{event_name} has started!")


def main():
    print("Welcome to the Countdown Application!")

    event_date = get_event_date()
    event_name = get_event_name()

    print("\nCountdown:")
    countdown_timer(event_date, event_name)


if __name__ == "__main__":
    main()
