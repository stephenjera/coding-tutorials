from urllib.request import urlopen

story = urlopen("http://sixty-north.com/c/t.txt")
words = []
for line in story:
    line_words = line.decode("utf-8").split()
    for word in line_words:
        words.append(word)
story.close()

def print_words():
    for word in words:
        print(word)