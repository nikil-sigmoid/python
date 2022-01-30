# regular function
def add_number(num):
    value = num + 20
    return value


result = add_number(20)
print(result)
print()

# lambda function
result = lambda x: x + 20
print(result(20))
print()

x = lambda a, b: a * b
print(x(10, 20))
