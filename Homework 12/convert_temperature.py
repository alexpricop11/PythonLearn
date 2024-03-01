def convert_temperature(temperature, unit):
    if unit.upper() == "C":
        converted_temperature = (temperature * 9 / 5) + 32
    elif unit.upper() == "F":
        converted_temperature = (temperature - 32) * 5 / 9
    else:
        print("Invalit unit, enter 'C' or 'F'")
        return temperature, unit

    return converted_temperature, converted_unit


while True:
    try:
        temperature_input = float(input("Enter the temperature: "))
        unit_input = input("Enter the currient unit (C/F): ").upper()
        converted_temp, converted_unit = convert_temperature(temperature_input, unit_input)
        print(f"Conerted temperature {converted_temp} {unit_input}")
        break
    except ValueError:
        print("Enter valid temperature")
