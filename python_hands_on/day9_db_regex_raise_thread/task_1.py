try:
    input_pin = int(input("Please enter your ATM PIN: "))

    while input_pin != 1234:
        input_pin = int(input("Wrong PIN! Please enter your ATM PIN again: "))

    print("Welcome to ABC Bank")
except:
    print("Please enter input is valid format")
