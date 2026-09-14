# Dictionary:
# A dictionary is suitable because each motor has labelled information.
# Lists are used for the fault codes because a motor can have multiple faults.
# A set is used to store unique fault codes.

motors = {
    "M-101": {
        "location": "Workshop A",
        "rated_power_kw": 5.5,
        "temperature": 72,
        "status": "RUNNING",
        "fault_codes": ["F01", "F03", "F01"]
    },

    "M-102": {
        "location": "Workshop B",
        "rated_power_kw": 7.5,
        "temperature": 88,
        "status": "RUNNING",
        "fault_codes": ["F07", "F03"]
    },

    "M-103": {
        "location": "Pump Station",
        "rated_power_kw": 11.0,
        "temperature": 79,
        "status": "SERVICE REQUIRED",
        "fault_codes": ["F12", "F07"]
    }
}

# Display complete record for M-102
print("Complete record for M-102:")
print(motors["M-102"])

# Update M-102 status
motors["M-102"]["status"] = "OVERHEAT"

print("\nUpdated M-102 status:", motors["M-102"]["status"])

# Counter for overheated motors
overheated_count = 0

# Set for unique fault codes
unique_faults = set()

# Loop through every motor
print("\nMotor information:")

for motor_id, motor in motors.items():

    print("ID:", motor_id)
    print("Location:", motor["location"])
    print("Temperature:", motor["temperature"], "°C")
    print("Status:", motor["status"])
    print()

    # Count temperatures above 85°C
    if motor["temperature"] > 85:
        overheated_count += 1

    # Add fault codes to the set
    unique_faults.update(motor["fault_codes"])

# Display results
print("Motors above 85 °C:", overheated_count)
print("Unique fault codes:", unique_faults)
print("Number of unique faults:", len(unique_faults))