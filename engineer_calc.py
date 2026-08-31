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
    """Print the menu by iterating over options from build_menu."""
    options = build_menu()
    print("\n--- Engineering Calculator Menu ---")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def safe_float_input(prompt):
    """Prompt for user input and convert to float, raising ValueError on failure."""
    raw_val = input(prompt)
    return float(raw_val)


def main():
    running = True
    while running:
        display_menu()
        choice = input("Select an option (1-7): ")

        try:
            if choice == "1":
                voltage = safe_float_input("Enter voltage (V): ")
                current_input = input(
                    "Enter current (A) or press Enter for default: "
                )
                current = (
                    DEFAULT_CURRENT
                    if current_input == ""
                    else float(current_input)
                )

                try:
                    resistance = calc_resistance(voltage, current)
                    print(f"Resistance = {resistance:.2f} ohms")
                except ZeroDivisionError:
                    print("Error: Current cannot be zero.")

            elif choice == "2":
                voltage = safe_float_input("Enter voltage (V): ")
                resistance = safe_float_input("Enter resistance (ohms): ")
                try:
                    power = calc_power(voltage, resistance)
                    print(f"Power = {power:.2f} W")
                except ZeroDivisionError:
                    print("Error: Resistance cannot be zero.")

            elif choice == "3":
                val = safe_float_input("Enter measurement in mm: ")
                print(f"Converted value: {mm_to_inches(val):.2f} inches")

            elif choice == "4":
                val = safe_float_input("Enter measurement in inches: ")
                print(f"Converted value: {inches_to_mm(val):.2f} mm")

            elif choice == "5":
                val = safe_float_input("Enter measurement in cm: ")
                print(f"Converted value: {cm_to_inches(val):.2f} inches")

            elif choice == "6":
                val = safe_float_input("Enter measurement in inches: ")
                print(f"Converted value: {inches_to_cm(val):.2f} cm")

            elif choice == "7":
                running = False
                print("Program closed.")

            else:
                print("Invalid menu option.")

        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()