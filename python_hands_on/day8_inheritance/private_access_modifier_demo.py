class Car:

    def __init__(self, color, engine, tyre_color):
        # private variables(two underscores as prefix), only accessible within the class itself
        self.__color_of_car = color
        self.__engine_type = engine
        self.__color_of_tyre = tyre_color

    def print_car_info(self):
        print(self.__color_of_car)
        print(self.__engine_type)
        print(self.__color_of_tyre)


mercedes = Car('silver', 'petrol', 'black')
mercedes.print_car_info()
print()

print(mercedes._Car__color_of_car)
print(mercedes._Car__engine_type)
print(mercedes._Car__color_of_tyre)