from collections import Counter
import sys
import re


WORDS_COUNT_TO_SHOW = 10


def load_data(filepath, chunk_size=1024):
    with open(filepath, "r", encoding="utf-8") as file:
        while True:
            text_peace = file.read(chunk_size)
            if not text_peace:
                break
            yield text_peace


def get_most_frequent_words(filepath, words_count):
    c = Counter()
    for peace in load_data(filepath):
        peace = peace.lower()
        c.update(re.findall(r"(\w+)", peace))
    frequent_words = c.most_common()[:words_count]
    print_result(frequent_words)


def print_result(frequent_words):
    for index in range(len(frequent_words)):
        print(str(frequent_words[index][1]) + ":" + str(frequent_words[index][0]))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_most_frequent_words(sys.argv[1], WORDS_COUNT_TO_SHOW)


