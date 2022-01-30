def greet_people(names):
    for name in names:
        print(f"Hello {name.title()}, welcome to the party")


names_list = ["John", "James", "Terry"]
greet_people(names_list)