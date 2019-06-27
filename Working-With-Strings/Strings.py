# This file will contain multiple examples of how not to work with strings
# USE LISTS UNTIL GIVEN NO CHOICE! STRINGS ARE IMMUTABLE 

# example string (this upper function is being special)
word = "this should be uppercase!"
print(word.upper())
cap_test = "Hello world"
print("This is old " + cap_test)
cap_test = cap_test.upper()  # Result of upper function need a place to go
print("This is new: " + cap_test)  # upper() function does not work??

# Taking a string and changing a letter to different case
string_input = input("Enter string: ")
string_length = len(string_input)

# print(str(string_length) + " " + string_input)  # Result check

# Choose letter to change
print("Which letter index should be changed?")  # Bad habits from C edit to use input only
index = input("Choose a number between 0 and " + str(string_length - 1))
print("index type is " + str(type(index)))

# Print the result
output = str(string_input[int(index)])
print("Output is: " + str(output))
output = output.upper()  # convert selected letter to uppercase
print("New output is: " + str(output))
print("output is " + str(output))  # Check output value
string_input[int(index)] = output  # Does not work like C need new method
print(string_input)
