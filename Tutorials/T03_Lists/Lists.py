# This code uses lists to change a letter to uppercase

input_string = input("Please enter you string: ")
# Example of type hinting lists
input_list = [str]  # List to store user input

# Loop to copy string to list
for x in range(len(input_string)):  # Range function count from 0, increments of 1
    input_list.append(input_string[x])
    print(len(input_string)),  # Use comma to end loops
print(input_list)

# Choose which character should be changed
change_index = input("Choose an index from 0 to " + str(len(input_string) - 1) + ": ")

input_list[int(change_index)] = input_list[int(change_index)].upper()
# temp = input_list[change_index].upper()
# print(temp)
print(input_list)
