# Filtering out even numbers
numbers = [20, 23, 1, 4, 99, 21, 32, 44, 67, 98, 80]

even_numbers = list(filter(lambda x: (x%2 == 0), numbers))
print(even_numbers)
print()


# Printing numbers greater than 10.
numbers = [20, 23, 1, 4, 99, 21, 32, 44, 67, 98, 80]

greater_than_value = list(filter(lambda x: x > 10, numbers))
print(greater_than_value)