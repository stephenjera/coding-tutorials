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

            else:
                word = input("Enter a word: ")  # Keep looping until only letters entered
        except TypeError:  # This shouldn't trigger as all inputs will be strings
            print("Not a string")

    print(word[0])

# Main code


pig_latin()

