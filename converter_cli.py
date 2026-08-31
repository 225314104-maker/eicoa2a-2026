from unit_converter import (
    cm_to_inches,
    inches_to_cm,
    inches_to_mm,
    mm_to_inches,
)

# Independent function assertions
assert round(mm_to_inches(25.4), 2) == 1.0
assert inches_to_mm(1) == 25.4
assert round(cm_to_inches(2.54), 2) == 1.0
assert inches_to_cm(2) == 5.08

print("All conversion unit tests passed independently!")

# Display all conversion docstrings
print("\n--- Unit Converter Docstrings ---")
print("1. mm_to_inches:")
print(mm_to_inches.__doc__)

print("2. inches_to_mm:")
print(inches_to_mm.__doc__)

print("3. cm_to_inches:")
print(cm_to_inches.__doc__)

print("4. inches_to_cm:")
print(inches_to_cm.__doc__)