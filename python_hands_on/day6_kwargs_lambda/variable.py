def print_full_name(first_name, last_name):
    global full_name
    full_name = f"{first_name.title()} {last_name.title()}"
    print(full_name)


def day_info():
    print("Today is Wednesday")
    print(full_name)


print_full_name("James", "Bond")
day_info()
