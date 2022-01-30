def create_person(first_name, last_name):
    person = {
        'first': first_name,
        'last': last_name
    }
    return person


while True:
    first_name = input("Please enter your first name: ")
    if first_name.lower() == 'quit':
        break
    last_name = input("Please enter your last name: ")
    if last_name.lower() == 'quit':
        break
    actor = create_person(first_name, last_name)
    print(f"First Name: {actor['first']}")
    print(f"Last Name: {actor['last']}")
    print()