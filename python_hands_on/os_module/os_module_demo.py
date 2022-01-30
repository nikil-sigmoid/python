import os
from datetime import datetime

# All attributes and methods in this module
print(dir(os))

# Get current directory
print(os.getcwd())

# To change the directory
os.chdir('/Users/nik/Desktop')

print(os.getcwd())

# To list files/directories, we can provide the dir, by default in current directory
print(os.listdir())


# To create directory
# Method-1, mkdir()
os.mkdir('OS_demo')

# Method-2, makedirs() is used to create multiple intermediate directories
os.makedirs('OS_demo2/Sub_dir_1/sub_sub_dir2')

# To delete directories
# Method-1, rmdir()
os.rmdir('OS_demo')

# Method-2, removedirs() is used to create multiple intermediate directories
os.removedirs('OS_demo2/Sub_dir_1/sub_sub_dir2')

# To rename file/folder
# s.rename('text.txt', 'demo.txt')

print(os.listdir())

os.chdir('/Users/nik/Desktop')
# To get info about file using stat)()
print(os.stat('demo.txt'))

# modified time
mod_time = os.stat('demo.txt').st_mtime # it is a timestamp
print(datetime.fromtimestamp(mod_time))

print()
# walk() is a generator, it can be used to traverse directory hierarchy/tree to show all folders and files in the directory
# It can be used in web application also to get all files and folders
for dirpath, dirnames, filenames in os.walk('/Users/nik/Desktop'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()


# To get environment variables, using environ()
# To get HOME environment variable
print(os.environ.get('HOME'))

file_path = os.environ.get('HOME') + 'test.txt'
print(file_path) # Missing /

# Better way, using os.path.join()
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# Now to create that file
with open(file_path, 'w') as f:
    pass


# More functionalities of os.path()
# To get file name
print(os.path.basename('/tmp/test.txt'))

# To get directory name
print(os.path.dirname('/tmp/test.txt'))

# To get both file and directory separately
print(os.path.split('/tmp/test.txt'))

# Get file name and extension separately
print(os.path.splitext('/tmp/test.txt'))

# To check if folder/file exists
print(os.path.exists('/tmp/fojndkf'))

# To check if its directory
print(os.path.isdir('/tmp/fojndkf'))

# To check if its a file
print(os.path.isfile('/tmp/fojndkf'))

# Attributes and methods in os.path()
print(dir(os.path))

