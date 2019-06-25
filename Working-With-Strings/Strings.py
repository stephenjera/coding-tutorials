# This file will contain multiple examples of working with strings

# Taking a string and changing a letter to different case
string_input = input("Enter string: ")
string_length = len(string_input)

print(str(string_length) + " " + string_input)  # Result check

# Choose letter to change
print("Which letter index should be changed?")  # Bad habits from C edit to use input only
print("Choose a number between 0 and " + str(string_length - 1))
index = input()

# Print the result
output = string_input[int(index)]
output.upper()  # convert selected letter to uppercase
print("output is " + str(output))  # Check output value
string_input[int(index)] = output  # Does not work like C need new method
print(string_input)



