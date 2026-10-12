try:
    with open("machine_log.txt", "r") as file:
        for line in file:
            cleaned_line = line.strip()

            if cleaned_line == "":
                continue

            print(cleaned_line)

except FileNotFoundError:
    print("Log file is missing.")