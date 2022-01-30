# Writing to the files
# if file is already exists it'll override, otherwise it'll create a new file
# it will also overwrite if we try to write to place where already content exists
with open('test2.txt', 'w') as f:
    f.write('Test')
    # f.write('Test')
    f.seek(0)
    f.write('R')

# To both read and write, we can use 'r+'

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# to read and write binary files, we need to use 'rb' and 'wb'
with open('dog.jpg', 'rb') as rf:
    with open('dog_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


# reading and writing in chunks
with open('dog.jpg', 'rb') as rf:
    with open('dog_copy2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
