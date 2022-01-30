# file objects

f = open('test.txt', 'r')

print(f.mode)

# To avoid leaks
f.close()

