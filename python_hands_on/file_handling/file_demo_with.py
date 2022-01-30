# file objects
# Reading from files

with open('test.txt', 'r') as f:
    # f.readlines() will give all lines
    # f.readline() will give only one line
    file_contents = f.read()
    print(file_contents)


# file object will be closed automatically, you still have access to it, but you can't read from the file
print()
print(f.closed)
print()


with open('test.txt', 'r') as f:
    file_contents = f.readline()
    print(file_contents, end='')

    file_contents = f.readline()
    print(file_contents, end='')


print()
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')


print()
print()

with open('test.txt', 'r') as f:

    # It will print only first 100 characters from the file
    file_contents = f.read(100)
    print(file_contents, end='')


print()
print()

with open('test.txt', 'r') as f:

    # It will print only first 100 characters from the file
    file_contents = f.read(100)
    print(file_contents, end='')

    # It will print next 100 characters
    file_contents = f.read(100)
    print(file_contents, end='')

print()
print()


# If our pointer goes to the end of the file, it will just return empty string
# To avoid that...
with open('test.txt', 'r') as f:

    size_to_read = 10

    file_contents = f.read(size_to_read)

    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = f.read(size_to_read)


# Position of file pointer using tell()
with open('test.txt', 'r') as f:

    size_to_read = 10

    f.contents = f.read(size_to_read)

    print(f.tell())


print()

# seek() to set the file pointer
with open('test.txt', 'r') as f:

    size_to_read = 10

    file_contents = f.read(size_to_read)
    print(file_contents)

    # setting file pointer to the beginning of file
    f.seek(0)

    file_contents = f.read(size_to_read)
    print(file_contents)

print()



