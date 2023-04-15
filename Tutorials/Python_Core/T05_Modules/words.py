from urllib.request import urlopen


words = []


def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt")
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            words.append(word)
    story.close()


def print_words():
    for word in words:
        print(word)

print(__name__)

if __name__=="__main__":
    fetch_words()
    print_words()