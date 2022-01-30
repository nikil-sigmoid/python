# https://www.youtube.com/watch?v=NIWwJbo-9_8

# try: it tries executing a piece of code
# except: catches the exception, put specific exception first(FileNotFoundError, etc) and general Exception in the end
# else: Only runs if there is no exception
# finally: Always runs irrespective of exception or not
# raise: It raises custom exception

try:
    f = open('some_file.txt')
    if f.name == 'some_file.txt':
        raise Exception("File is couldn't be opened.")
except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print("Execute it irrespective of exception or not.")

