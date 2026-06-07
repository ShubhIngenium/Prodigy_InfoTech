# Temperature Conversion Program

This is a simple Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin.

## Features

- Accepts a numeric temperature value from the user
- Accepts the original unit: `Celsius`, `Fahrenheit`, or `Kelvin`
- Converts the input value into the other two temperature scales
- Displays the converted values with two decimal places

## Usage

1. Run the program:

```bash
python main.py
```

2. Enter a temperature value when prompted.
3. Enter the original unit when prompted.

Example input:

```text
Enter temperature value: 25
Enter the original unit (Celsius, Fahrenheit, Kelvin): Celsius
```

Example output:

```text
25.00° Celsius is:
- 77.00° Fahrenheit
- 298.15° Kelvin
```

## Supported units

- `Celsius` (or `C`)
- `Fahrenheit` (or `F`)
- `Kelvin` (or `K`)

## Test values

- `25` Celsius → `77.00° Fahrenheit`, `298.15° Kelvin`
- `32` Fahrenheit → `0.00° Celsius`, `273.15° Kelvin`
- `0` Kelvin → `-273.15° Celsius`, `-459.67° Fahrenheit`
- `100` Celsius → `212.00° Fahrenheit`, `373.15° Kelvin`
- `212` Fahrenheit → `100.00° Celsius`, `373.15° Kelvin`
- `373.15` Kelvin → `100.00° Celsius`, `212.00° Fahrenheit`

## Notes

- The program validates numeric temperature input.
- If the unit is invalid, it asks again for a supported unit.
