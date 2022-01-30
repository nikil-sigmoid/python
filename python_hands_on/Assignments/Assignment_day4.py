sentence = "Fare: $18,369 - $120,379*"
new_sentence = ""

for char in sentence:
    if char.isnumeric() or char == "$":
        new_sentence += char

print(new_sentence)

list_numbers = []
for number in new_sentence.split('$'):
    if number.isnumeric():
        list_numbers.append(int(number))

print(list_numbers)
print(type(list_numbers[0]))

if list_numbers[0] > 0 and list_numbers[1] > 0:
    print("Both values are greater than 0.")
else:
    print("Both values are not greater than 0.")


print()
print('-------------------------------------------')
print('Another approach')
print()

text = "Fare: $18,369 - $120,379*"

text_range = text[6:]

special_chars = '$,*'
new_text_range = ''

for value in text_range:
    if value in special_chars:
        continue
    else:
        new_text_range += value

print(new_text_range)

value1 = int(new_text_range.split('-')[0])
value2 = int(new_text_range.split('-')[1])

if value1 > 0 and value2 > 0:
    print("Both the price values are greater than 0.")
else:
    print("One of the values is not greater than 0.")