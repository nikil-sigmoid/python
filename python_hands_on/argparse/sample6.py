import json
import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', type=str)


# x =  '{ "name":"John", "age":30, "city":"New York"}'

x = parser.parse_args()

# parse x:
y = json.loads(x.x)

# the result is a Python dictionary:
print(type(y["age"]))
