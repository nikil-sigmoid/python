sentence = "Fare:$18,369-$120,379"
new_sentence = ""
prev_char_is_num = ""

for char in sentence:
    if char.isnumeric():
        if prev_char_is_num.isnumeric() or prev_char_is_num == "," or len(new_sentence) == 0:
            new_sentence += char
        else:
            new_sentence += " "
            new_sentence += char
    prev_char_is_num = char

list_numbers = []

for number in new_sentence.split(" "):
    list_numbers.append(int(number))

print(list_numbers)
print(type(list_numbers[0]))

if list_numbers[0] > 0 and list_numbers[1] > 0:
    print("Both values are greater than 0.")
else:
    print("Both values are not greater than 0.")

