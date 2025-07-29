'''
# READING FILES ---------------------
'''

#method 1
'''
file = open("gamma.txt", encoding="utf-8")

print(file.read())

file.close()
'''

#method 2 - no need to close the file

with open("gamma.txt", encoding="utf-8") as file:
    print(file.read()) # reads the whole file
    print(file.read(10)) # reads the first 10 characters
    print(file.read(10)) # reads the next 10 characters
    print(file.readline()) # reads the next line

with open("gamma.txt", encoding="utf-8") as file:
    print(file.readlines()) # reads the whole file and returns a list of lines

with open("gamma.txt", encoding="utf-8") as file:
    for line in file:
        print(line) # reads the whole file and returns a list of lines


'''
# WRITING TO FILES ---------------------
'''

# if file is empty, write to it
with open("terra_world.txt", "a", encoding="utf-8") as file:
    file.write("Hello, world!")

# if file is not empty, write to it
with open("gamma_world.txt", "a", encoding="utf-8") as file:
    file.write("Hello, world!")

# overwrite the existing file content
with open("terra_world.txt", "w", encoding="utf-8") as file:
    file.write("Hello, terra!")


'''
# DELETING FILES ---------------------
'''

import os

os.remove("terra_world.txt")

