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
    input_list = []  # List to store user input
    for x in range(len(input_string)):  # Range function count from 0, increments of 1
        input_list.append(input_string[x]),
        # print(len(input_string)),  # Use comma to end loops
    return input_list


def pig_latin():
    """Convert word to pig latin, takes a string as input"""
    control = True
    while control:
        try:
            # word = ""  # Any non-alphabet character will work
            word = input("Enter a word: ")
            # Check if input only has letters
            if word.isalpha():
                control = False  # Loop escape
                # Algorithm goes here
                # Should only have letters at this point
                # Stings immutable need to convert to lists

                vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')  # Tuple is immutable
                if word.startswith(vowels):
                    word_list = string_to_list(word)
                    word_list.append("-yay")
                else:
                    word_list = string_to_list(word)  # startswith doesn't work on lists
                    word_list.append("-")
                    word_list.append(word[0])  # Can try word_list[0] to see if result is same
                    word_list.append("ay")
                    del[word_list[0]]
                return ''.join(word_list)  # Return a string
            # else:
            #    word = input("Enter a word: ")  # Keep looping until only letters entered
        except TypeError:  # This shouldn't trigger as all inputs will be strings
            print("Not a string")

    #print(word[0])

# Main code


print(pig_latin())
#print(string_to_list("test"))

#list1 = ["a", "b", "c"]
'''test = ["a", "b", "h"]
test2 = "ello"
print(test2.startswith)'''
#print(list1)
#print(''.join(list1))
