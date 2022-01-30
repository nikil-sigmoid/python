colour_names = ["Black", "Red", "Blue"]
print(colour_names)

# Adding a new colour at the end
colour_names.append("Brown")
print(colour_names)

# Adding a colour at 2nd index(considering 2nd position means 2nd index)
colour_names.insert(2, "Pink")
print(colour_names)


# Class assignment [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares_of_numbers =  []
for i in range(1, 11):
    squares_of_numbers.append(i**2)

for num in squares_of_numbers:
    print(num)