topping_names = []
prompt = "Enter a series of pizza toppings: "

active = True

while active:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    elif topping.lower() == 'basil leaves' or topping.lower() == 'cherry':
        print("Sorry! We don't have basil leaves and cherry currently.")
    else:
        topping_names.append(topping)

print("Following toppings will be added to the pizza: ")
for topping  in topping_names:
    print(topping.title())
