class Car:

    def __init__(self, color, engine, tyre_color):

        # public variables(accessible everywhere)
        self.color_of_car = color
        self.engine_type = engine
        self.color_of_tyre = tyre_color


mercedes = Car('silver', 'petrol', 'black')

print(mercedes.color_of_car)
print(mercedes.engine_type)
print(mercedes.color_of_tyre)
