from ohms_law import calc_power, calc_resistance
from unit_converter import (
    cm_to_inches,
    inches_to_cm,
    inches_to_mm,
    mm_to_inches,
)

DEFAULT_CURRENT = 0.5


def build_menu():
    """Generate and return a list of available menu options."""
    return [
        "Calculate Resistance",
        "Calculate Power",
        "Convert mm to Inches",
        "Convert Inches to mm",
        "Convert cm to Inches",
        "Convert Inches to cm",
        "Exit",
    ]


def display_menu():
    """Print the menu by iterating over the options from build_menu."""
    options = build_menu()
    print("\n--- Engineering Calculator Menu ---")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def main():
    running = True
    while running:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current_input = input(
                "Enter current (A) or press Enter for default: "
            )

            if current_input == "":
                current = DEFAULT_CURRENT
            else:
                current = float(current_input)

            try:
                resistance = calc_resistance(voltage, current)
                print("Resistance =", resistance, "ohms")
            except ZeroDivisionError:
                print("Error: Current cannot be zero.")

        elif choice == "2":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (ohms): "))
            try:
                power = calc_power(voltage, resistance)
                print("Power =", power, "W")
            except ZeroDivisionError:
                print("Error: Resistance cannot be zero.")

        elif choice == "3":
            value = float(input("Enter measurement in mm: "))
            print("Converted value:", mm_to_inches(value), "inches")

        elif choice == "4":
            value = float(input("Enter measurement in inches: "))
            print("Converted value:", inches_to_mm(value), "mm")

        elif choice == "5":
            value = float(input("Enter measurement in cm: "))
            print("Converted value:", cm_to_inches(value), "inches")

        elif choice == "6":
            value = float(input("Enter measurement in inches: "))
            print("Converted value:", inches_to_cm(value), "cm")

        elif choice == "7":
            running = False
            print("Program closed.")

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()