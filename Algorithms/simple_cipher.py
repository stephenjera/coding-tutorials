def write_file(name):
    """Creates a file and writes to it"""
    try:
        file = open(name, "w")  # Open file for writing
        file.write(input("Enter some text: "))  # Get user input for the file
    finally:
        file.close()


def cipher():
    """Apply cipher to text in file"""
    with open(file_name) as f:
        text = f.read()  # Doesn't print as expected
        print("Before cipher: ", text)
        text = text[::-1]  # Doesn't print as expected
        print("After cipher: ", text)
    return text


# file_name = input("Enter a file name with the .txt extension:  ")
file_name = "test.txt"
write_file(file_name)  # Create file and write

try:
    file = open(file_name, "w")  # Open file for writing
    file.write(cipher())  # Get user input for the file
finally:
    file.close
'''
with open(file_name) as f:
    f.write(cipher())  # Write cipher to file
    '''
