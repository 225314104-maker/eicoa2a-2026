import random
from tabulate import tabulate

# Dictionary containing component IDs and measured voltages
components = {
    "ECU-101": 4.96,
    "ECU-102": 5.08,
    "ECU-103": 4.88,
    "ECU-104": 5.02,
    "ECU-105": 5.15,
    "ECU-106": 4.99,
    "ECU-107": 4.91,
    "ECU-108": 5.05
}

# Tuple containing fixed voltage limits
voltage_tolerance = (4.90, 5.10)

# Unpack the tuple
minimum_voltage, maximum_voltage = voltage_tolerance

# Make random testing repeatable
random.seed(42)

# Randomly select four different components
selected_components = random.sample(list(components.keys()), 4)

# List to store inspection results
inspection_rows = []

# Set to store failed component IDs
failed_components = set()

# Counters
pass_count = 0
fail_count = 0

# Store voltages for calculating the average
inspected_voltages = []

# Check each selected component
for component_id in selected_components:

    voltage = components[component_id]

    inspected_voltages.append(voltage)

    if minimum_voltage <= voltage <= maximum_voltage:
        result = "PASS"
        pass_count += 1

    else:
        result = "FAIL"
        fail_count += 1
        failed_components.add(component_id)

    inspection_rows.append([component_id, voltage, result])

# Display inspection table
print("Inspection Results:")
print(tabulate(
    inspection_rows,
    headers=["Component ID", "Voltage (V)", "Result"],
    tablefmt="grid"
))

# Calculate average voltage
average_voltage = sum(inspected_voltages) / len(inspected_voltages)

# Display summary
print("\nAverage voltage:", round(average_voltage, 2), "V")
print("PASS:", pass_count)
print("FAIL:", fail_count)
print("Failed components:", failed_components)