# task 1.1
number_of_people = int(input("How many people are there in the dinner group?: "))

if number_of_people > 8:
    print("They will have to wait for a table")
else:
    print("Their table is ready")

# task 1.2
number = int(input("Please enter any number: "))
if number%10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# task 1.32
full_name = input("Enter your full name: ")
current_year = int(input("Enter the current year: "))

print(f"You entered your name as - {full_name}")
if current_year%2 == 0:
    print(f"Year {current_year} is an even year.")
else:
    print(f"Year {current_year} is an odd year.")
