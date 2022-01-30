def make_pizza(size, *toppings):
    print(f"Making {size} - inches pizza with following toppings")
    for topping in toppings:
        print(f"{topping.title()}")


def make_chocolate_milk_shake(size, *ingredients):
    print(f"Here is your {size}  chocolate shake with following ingredients")
    for ingredient in ingredients:
        print(f"{ingredient.title()}")


def day_info():
    print("Today is Wednesday")


