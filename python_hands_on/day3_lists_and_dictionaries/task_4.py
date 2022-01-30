current_users = ["Abhi34", "Alice21", "tim12", "JOHN55", "Ron589"]

new_users = ["Robin3", "Tim12", "Ria99", "Abhi34", "Karan89"]

current_users_copy = []
for user in current_users:
    current_users_copy.append(user.lower())

for user in new_users:
    if user.lower() in current_users_copy:
        print(f"The username {user} is not available, person will need to enter a new username.")
    else:
        print(f"The username {user} is available.")
