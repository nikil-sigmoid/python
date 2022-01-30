def create_person(first_name, last_name):
    person = {
        'first': first_name,
        'last': last_name
    }
    return person


actor = create_person("James", "Bond")
print(f"First Name - {actor['first']}")
print(f"Last Name - {actor['last']}")
