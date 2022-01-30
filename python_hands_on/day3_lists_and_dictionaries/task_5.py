user_info = {
    'first_name': 'john',
    'last_name': 'anderson',
    'age': 38,
    'city': 'southampton'
}

for k, v in user_info.items():
    print(f"{k.title()} = {str(v).title()}")