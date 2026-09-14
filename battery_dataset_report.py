# List containing the battery voltage readings
voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]

# Counters for each battery classification
good_count = 0
marginal_count = 0
low_count = 0

# List to store low-voltage readings
low_voltages = []

# Loop through each voltage
for number, voltage in enumerate(voltages, start=1):

    if voltage > 12.5:
        classification = "GOOD"
        good_count += 1

    elif voltage >= 11.5:
        classification = "MARGINAL"
        marginal_count += 1

    else:
        classification = "LOW"
        low_count += 1
        low_voltages.append(voltage)

    print("Reading", number, ":", voltage, "V -", classification)

# Calculations
total_voltage = sum(voltages)
average_voltage = total_voltage / len(voltages)
highest_voltage = max(voltages)
lowest_voltage = min(voltages)

# Display results
print("\nGOOD:", good_count)
print("MARGINAL:", marginal_count)
print("LOW:", low_count)

print("Low-voltage readings:", low_voltages)

print("Total voltage:", total_voltage, "V")
print("Average voltage:", round(average_voltage, 2), "V")
print("Highest voltage:", highest_voltage, "V")
print("Lowest voltage:", lowest_voltage, "V")

# Search for 12.1 V
if 12.1 in voltages:
    print("12.1 V was recorded.")
else:
    print("12.1 V was not recorded.")