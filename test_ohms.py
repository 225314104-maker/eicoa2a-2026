from ohms_law import calc_power, calc_resistance

# Resistance tests
result = calc_resistance(9, 0.03)
print("Resistance =", result, "ohms")

assert calc_resistance(9, 0.03) == 300
assert calc_resistance(24, 2) == 12

# Exercise 1 tests: P = V^2 / R
assert calc_power(10, 5) == 20.0
assert calc_power(12, 6) == 24.0

print("\n--- Docstrings ---")
print(calc_resistance.__doc__)
print(calc_power.__doc__)