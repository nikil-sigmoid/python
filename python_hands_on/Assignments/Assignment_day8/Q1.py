class Computer:
    def __init__(self, make, ram, storage):
        self.make_name = make
        self.ram_available = ram
        self.__storage_available = storage


class Mobile(Computer):
    def __init__(self, make, ram, storage, model):
        Computer.__init__(self, make, ram, storage)
        self.model_name = model


apple = Mobile("Apple", "8GB", "128GB", "iPhone 11")
print(f"Make Name: {apple.make_name}")
print(f"Available RAM: {apple.ram_available}")

# Below statement will give an error
# print(f"Available Storage: {apple.__storage_available}")
print(f"Model Name: {apple.model_name}")
