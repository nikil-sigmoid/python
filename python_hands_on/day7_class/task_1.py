class Pizza_Makers:

    def __init__(self, size, crust):
        self.size_of_pizza = size
        self.pizza_crust = crust

    def pizza_info(self):
        print(f"Pizza is {self.size_of_pizza} inches in size with {self.pizza_crust} crust.")


small_pizza = Pizza_Makers(8, 'thin')
large_pizza = Pizza_Makers(14, 'regular')
small_pizza.pizza_info()
large_pizza.pizza_info()