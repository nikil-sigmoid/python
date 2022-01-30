people = []


def full_name(first_name, last_name):
    name = f"{first_name} {last_name}"
    return name


while True:
    print("Please enter your first name and last name")
    print("Type 'quit' to exit anytime")
    f_name = input("First name = ")
    if f_name.lower() == 'quit':
        break
    l_name = input("Last name: ")
    if l_name.lower() == 'quit':
        break
    people.append(full_name(f_name, l_name))

for name in people:
    print(name)
