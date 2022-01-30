class Calculator:

    def add(self, number1, number2):
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")

    def subtract(self, number1, number2):
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")

    def multiply(self, number1, number2):
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")

    def divide(self, number1, number2):
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")


obj = Calculator()
# obj.add(10, 2)
# obj.subtract(10, 2)
# obj.multiply(10, 2)
# obj.divide(10, 2)

