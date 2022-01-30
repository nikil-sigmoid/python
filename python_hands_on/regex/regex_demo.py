import re

text_value = "It's been nice day, Todey is Monday while it was Sunday yesterday"
value = re.search("d[a-z]y", text_value)

if value:
    print("Voila! it's a match")
else:
    print("Not a match")

print()

value = re.findall('day', text_value)
print(value)
print()

value = re.split("\s", text_value)
print(value)
print()

value = re.sub('day', 'night', text_value)
print(value)