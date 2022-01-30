L = ["This is Delhi \n", "This is Paris \n", "This is Tokyo \n", "This is London \n"]

# Writing to file
with open("test_file.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

# Appending to file
with open("test_file.txt", 'a') as file1:
    file1.write("Today")
