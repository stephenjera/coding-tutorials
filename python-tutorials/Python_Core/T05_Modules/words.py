import sys
from urllib.request import urlopen


def fetch_items(url):
    story = urlopen(url)
    words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            words.append(word)
    story.close()
    return words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_items(url)
    print_items(words)


print(__name__)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1]) # the oth argument is the module name
    else:
        main("http://sixty-north.com/c/t.txt")
    print(sys.argv)
