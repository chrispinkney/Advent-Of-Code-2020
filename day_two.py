def d2():
    print("--- Day 2: Password Philosophy ---")

    print("Part One")

    num_valid_passwords = 0
    with open ("files/passwords.txt", "r") as f:
        for line in f:
            min_max_number = line.split(" ")[0] # Splits on the space, returns both numbers. (ex: 2-5)
            min_times = int(min_max_number.split("-")[0]) # Split on the -, return the first number. (ex: 2)
            max_times = int(min_max_number.split("-")[1]) # Split on the -, return the second number. (ex: 5)
            character = line.split(" ", 1)[1][0] # Split on the space, return the character to test.
            password = line.split(": ", 1)[1] # Split on : , and return the password.
            num_times = 0

            for char in password:
                if character is char:
                    num_times += 1
            if num_times >= min_times and num_times <= max_times:
                num_valid_passwords += 1

    print(f"There are a total of: {num_valid_passwords} valid passwords in {f.name}")

    print("Part Two")

    num_valid_passwords = 0
    with open ("files/passwords.txt", "r") as f:
        for line in f:
            min_max_number = line.split(" ")[0] # Splits on the space, returns both numbers. (ex: 2-5)
            min_times = int(min_max_number.split("-")[0]) # Split on the -, return the first number. (ex: 2)
            max_times = int(min_max_number.split("-")[1]) # Split on the -, return the second number. (ex: 5)
            character = line.split(" ", 1)[1][0]  # Split on the space, return the character to test.
            password = line.split(": ", 1)[1]  # Split on : , and return the password.

            if password[min_times - 1] is character or password[max_times - 1] is character:
                if password[min_times - 1] != password[max_times - 1]:
                    num_valid_passwords += 1

    print(f"Oops, actually there are a total of: {num_valid_passwords} valid passwords in {f.name}")
