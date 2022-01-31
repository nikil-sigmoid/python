import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--list", nargs="+")

value = parser.parse_args()
print(value.list)
