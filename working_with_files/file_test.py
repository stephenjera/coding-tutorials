file = open("test.txt", "w") # Open file for writing
file.write("Hello World!")
file.close

file = open("test.txt", "r") # Open file for reading
print(file.read())
file.close()

input() # stop console closing
