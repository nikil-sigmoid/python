def get_full_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name


returned_full_name = get_full_name("James", "Bond")
print(returned_full_name)

