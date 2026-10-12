total_weight = 0.0
count = 0

try:
    with open("weights.txt", "r") as file:
        for line in file:
            try:
                weight = float(line.strip())
                total_weight += weight
                count += 1

            except ValueError:
                continue

    if count > 0:
        average_weight = total_weight / count
    else:
        average_weight = 0.0

    with open("weight_summary.txt", "w") as file:
        file.write("Engineering Weight Summary\n")
        file.write("--------------------------\n")
        file.write(f"Valid components: {count}\n")
        file.write(f"Total weight: {total_weight:.2f}\n")
        file.write(f"Average weight: {average_weight:.2f}\n")

    print("Summary successfully saved to weight_summary.txt")

except FileNotFoundError:
    print("Warning: weights.txt is missing.")