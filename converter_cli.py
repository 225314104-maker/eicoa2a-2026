from unit_converter import (
    cm_to_inches,
    inches_to_cm,
    inches_to_mm,
    mm_to_inches,
)


def main():
    """Interactive CLI driver for unit conversions."""
    print("--- Unit Converter CLI ---")
    print("1. Convert mm to Inches")
    print("2. Convert Inches to mm")
    print("3. Convert cm to Inches")
    print("4. Convert Inches to cm")

    choice = input("Select an option (1-4): ")

    try:
        if choice == "1":
            mm = float(input("Enter length in mm: "))
            print(f"Result: {mm_to_inches(mm):.2f} inches")
        elif choice == "2":
            inches = float(input("Enter length in inches: "))
            print(f"Result: {inches_to_mm(inches):.2f} mm")
        elif choice == "3":
            cm = float(input("Enter length in cm: "))
            print(f"Result: {cm_to_inches(cm):.2f} inches")
        elif choice == "4":
            inches = float(input("Enter length in inches: "))
            print(f"Result: {inches_to_cm(inches):.2f} cm")
        else:
            print("Invalid menu choice.")
    except ValueError:
        print("Error: Input must be a valid number.")


if __name__ == "__main__":
    main()