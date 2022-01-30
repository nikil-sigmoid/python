import re

text_value = "Todey is Monday while it was Sunday yesterday"
value = re.search("d[a-z]y", text_value)

if value:
    print("Yes there is a match")
else:
    print("No match")

print()

value = re.findall('day', text_value)
print(value)
print()

value = re.split("\s", text_value)
print(value)
print()

value = re.sub('day', 'night', text_value)
print(value)



