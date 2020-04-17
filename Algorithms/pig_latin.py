# 1. Store a list of words
# 2. For each word:
#    a. Append hyphen
#    b. If first letter is vowel
#       i. Append hyphen
#       else
#       i. Append first letter
#       ii. Append "ay" 
#       iii. Remove first letter 

# Function definitions


def string_to_list(input_string):
    """Copy string to list"""
    for x in range(len(input_string)):  # Range function count from 0, increments of 1
        input_list = [str]  # List to store user input
        input_list.append(input_string[x]),
        # print(len(input_string)),  # Use comma to end loops
    return input_string


def pig_latin():
    """Convert word to pig latin, takes a string as input"""
    control = True
    while control:
        try:
            # word = ""  # Any non-alphabet character will work
            word = input("Enter a word: ")
            # If input is not a letter
            if word.isalpha():
                control = False  # Loop escape
                # Algorithm goes here
                # Should only have letters at this point
                # Stings immutable need to convert to lists
                vowels = ('a', 'e', 'i', 'o', 'u')  # Removed to use lower() function, 'A', 'E', 'I', 'O', 'U')
                if word.startswith(vowels):
                    word
                else:
                    pass
            else:
                word = input("Enter a word: ")  # Keep looping until only letters entered
        except TypeError:  # This shouldn't trigger as all inputs will be strings
            print("Not a string")

    print(word[0])

# Main code


#pig_latin()
print(string_to_list("test"))
