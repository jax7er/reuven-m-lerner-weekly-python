def reverse_word(word: str):
    return word[::-1]


def unicode_map(word: str):
    return {letter: ord(letter) for letter in word}
