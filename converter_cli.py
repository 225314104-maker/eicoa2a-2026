from unit_converter import (
    cm_to_inches,
    inches_to_cm,
    inches_to_mm,
    mm_to_inches,
)

# --- Exercise 2: Independent Unit Tests ---
assert round(mm_to_inches(25.4), 2) == 1.00
assert round(inches_to_mm(1.0), 2) == 25.40
assert round(cm_to_inches(2.54), 2) == 1.00
assert round(inches_to_cm(2.0), 2) == 5.08
print("All conversion unit tests passed independently!")

# --- Exercise 2: Display Function Docstrings ---
print("\n--- Unit Converter Docstrings ---")
print("1. mm_to_inches:\n", mm_to_inches.__doc__)
print("2. inches_to_mm:\n", inches_to_mm.__doc__)
print("3. cm_to_inches:\n", cm_to_inches.__doc__)
print("4. inches_to_cm:\n", inches_to_cm.__doc__)


# --- Activity 3.2: Interactive CLI Driver ---
def main():
    print("\n--- Interactive Unit Converter CLI ---")
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