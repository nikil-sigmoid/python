class Car:

    def __init__(self, color, engine, tyre_color):
        # protected variables(single underscore), accessible only inside the class and its sub-classes
        self._color_of_car = color
        self._engine_type = engine
        self._color_of_tyre = tyre_color


class Test(Car):

    def print_info(self):
        print(self._color_of_car)
        print(self._engine_type)
        print(self._color_of_tyre)


obj = Test('white', 'diesel', 'black')
obj.print_info()
print()

print(obj._color_of_car)
print(obj._engine_type)
print(obj._color_of_tyre)