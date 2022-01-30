class Car:

    # Constructor
    def __init__(self, color, engine):
        self.color_of_car = color
        self.engine_type = engine

    def print_car_info(self):
        print(f"Color of car: {self.color_of_car}")
        print(f"Type of Engine: {self.engine_type}")

    @staticmethod
    def number_of_steering_wheels():
        print("This car has 1 steering wheel.")


mercedes = Car('silver', 'petrol')
audi = Car('black', 'diesel')

mercedes.print_car_info()
print()
audi.print_car_info()
print()
mercedes.number_of_steering_wheels()
