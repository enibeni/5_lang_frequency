from collections import Counter
import sys
import re


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
        c.update(re.findall(r"(\w+)", peace))
    result = c.most_common()[:words_count]
    print_result(result)


def print_result(result):
    for i in range(0, len(result)):
        print(str(result[i][1]) + ":" + str(result[i][0]))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_most_frequent_words(sys.argv[1], 10)


