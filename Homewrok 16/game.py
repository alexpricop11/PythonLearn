import random


def roll_dice(num_dice, num_sides):
    dice_values = [random.randint(1, num_sides) for _ in range(num_dice)]
    total_sum = sum(dice_values)
    return dice_values, total_sum


def display_dice(dice_values):
    for value in dice_values:
        print(f"  -----  ")
        print(f" |     | ")
        print(f" |  {value}  | ")
        print(f" |     | ")
        print(f"  -----  ")


print("Welcome to the Dice Game!")

num_dice = int(input("Enter the number of dice: "))
num_sides = int(input("Enter the number of sides on each die: "))

while True:
    input("Press Enter to roll the dice (or type 'STOP' to stop): ")

    dice_values, total_sum = roll_dice(num_dice, num_sides)

    print("\nDice Values:")
    display_dice(dice_values)

    print(f"\nTotal Sum: {total_sum}")

    user_input = input("\nRoll again? (Press Enter to roll, type 'STOP' to stop): ")
    if user_input.upper() == "STOP":
        break

print("Thanks for playing!")
