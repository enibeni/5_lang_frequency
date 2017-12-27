from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
            return text


def find_most_frequent_words(text, words_count_to_show):
    c = Counter()
    for line in text.split("\n"):
        line = line.lower()
        c.update(re.findall(r"(\w+)", line))
    frequent_words = c.most_common(words_count_to_show)
    return frequent_words


def print_result(frequent_words):
    for word in frequent_words:
        print("{} : {}".format(word[0], word[1]))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = load_data(sys.argv[1])
        frequent_words = \
            find_most_frequent_words(text,
                                     words_count_to_show=10)
        print_result(frequent_words)
    else:
        print("enter path to a file")


