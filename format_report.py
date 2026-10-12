part_name = " hydraulic-valve-4      "
pressure = 45.6789

cleaned_name = part_name.strip().replace("-", " ").upper()

print(f"The {cleaned_name} operates at {pressure:.1f} bar.")