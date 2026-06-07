def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def parse_unit(value: str) -> str:
    normalized = value.strip().lower()
    if normalized in ["c", "celsius"]:
        return "celsius"
    if normalized in ["f", "fahrenheit"]:
        return "fahrenheit"
    if normalized in ["k", "kelvin"]:
        return "kelvin"
    raise ValueError("Unsupported temperature unit. Use Celsius, Fahrenheit, or Kelvin.")


def format_temperature(value: float, unit: str) -> str:
    return f"{value:.2f}° {unit.capitalize()}"


def main():
    print("Temperature Conversion Program")
    print("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    print()

    while True:
        try:
            temp_input = input("Enter temperature value: ").strip()
            temperature = float(temp_input)
            break
        except ValueError:
            print("Please enter a valid numeric temperature.")

    while True:
        try:
            unit_input = input("Enter the original unit (Celsius, Fahrenheit, Kelvin): ")
            original_unit = parse_unit(unit_input)
            break
        except ValueError as exc:
            print(exc)

    if original_unit == "celsius":
        converted_1 = celsius_to_fahrenheit(temperature)
        converted_2 = celsius_to_kelvin(temperature)
        print(f"\n{format_temperature(temperature, 'celsius')} is:")
        print(f"- {format_temperature(converted_1, 'fahrenheit')}")
        print(f"- {format_temperature(converted_2, 'kelvin')}")
    elif original_unit == "fahrenheit":
        converted_1 = fahrenheit_to_celsius(temperature)
        converted_2 = fahrenheit_to_kelvin(temperature)
        print(f"\n{format_temperature(temperature, 'fahrenheit')} is:")
        print(f"- {format_temperature(converted_1, 'celsius')}")
        print(f"- {format_temperature(converted_2, 'kelvin')}")
    else:
        converted_1 = kelvin_to_celsius(temperature)
        converted_2 = kelvin_to_fahrenheit(temperature)
        print(f"\n{format_temperature(temperature, 'kelvin')} is:")
        print(f"- {format_temperature(converted_1, 'celsius')}")
        print(f"- {format_temperature(converted_2, 'fahrenheit')}")


if __name__ == "__main__":
    main()
