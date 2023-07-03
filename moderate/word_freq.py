from collections import defaultdict

def setup_dict(book: list[str]) -> defaultdict:
    dictionary = defaultdict(int)
    for word in book:
        if word:
            dictionary[word.lower()] += 1
    return dictionary


def get_word_freq(dictionary: defaultdict, word: str) -> int:
    if (dictionary is None or word is None):
        return -1
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return 0


if __name__ == "__main__":
    book = ["one", "two", "two", "three", "three", "three", "four",
            "four", "four", "four"]
    dictionary = setup_dict(book)
    assert get_word_freq(dictionary, "three") == 3
