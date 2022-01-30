# obtain a new list where each element is 10 multiplied by original element
numbers = [1, 5, 32, 45, 88, 20]
new_numbers = list(map(lambda x: x * 10, numbers))
print(new_numbers)
print()

# Generate a new sorted list which is square of the numbers present in the list
numbers = [1, 5, 32, 45, 88, 20]
sorted_squared_numbers = sorted(list(map(lambda x: x * x, numbers)))
print(sorted_squared_numbers)
