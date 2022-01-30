class Car:

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def engine_type(self, engine):
        print(f"This car runs on {engine} engine")


mercedes = Car()  # mercedes is an object of class Car.
audi = Car()  # audi is an object of class Car.

# How to call a method
# object.method()

mercedes.start()
mercedes.stop()
mercedes.engine_type("petrol")





