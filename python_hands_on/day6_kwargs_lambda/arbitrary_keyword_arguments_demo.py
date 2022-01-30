def make_pizza(size, **toppings):
    print(f"Making {size} - inches pizza with following toppings")
    for v in toppings.values():
        print(f"Toppings = {v.title()} ")


make_pizza(size=10, first_topping='extra cheese')
make_pizza(size=12, first_topping='extra cheese', second_topping='capsicum', third_topping='jalapeno')