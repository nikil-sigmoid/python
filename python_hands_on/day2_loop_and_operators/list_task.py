cartoons = ['Doraemon', 'Nobita', 'Ninja']

# print(f"Hey {cartoons[0]}! You're invited to dinner tonight. Please be there by 8PM.")
# print(f"Hey {cartoons[1]}! You're invited to dinner tonight. Please be there by 8PM.")
# print(f"Hey {cartoons[2]}! You're invited to dinner tonight. Please be there by 8PM.")

# Task-1
for i in range(len(cartoons)):
    print(f"Hey {cartoons[i]}! You're invited to dinner tonight. Please be there by 8PM.")

print("-----------------------------------------")
print()

# Task-2
print("Hey guys! We've found a bigger dinner table.")
cartoons.insert(2, "micky mouse")
cartoons.append("chhota bheem")

for i in range(len(cartoons)):
    print(f"Hey {cartoons[i].title()}! You're invited to dinner tonight. Please be there by 8PM.")

print("---------------------------------------")
print()


# Task-3
for i in range(3):
    removed_item = cartoons.pop()
    print(f"Hey {removed_item}! I'm very sorry, table is not in good manner, next time please.")

print()
for i in range(len(cartoons)):
    print(f"Hey {cartoons[i].title()}! You're still invited to dinner tonight. Please be there by 8PM.")
