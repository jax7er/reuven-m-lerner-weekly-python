from itertools import zip_longest


def tr(find_chars: str, replace_chars: str):
    if not all(isinstance(x, str) for x in (find_chars, replace_chars)):
        raise TypeError

    len_find = len(find_chars)
    len_replace = len(replace_chars)

    if 0 in (len_find, len_replace):
        raise TypeError
    
    max_width = max(len_find, len_replace)

    find_chars = find_chars.ljust(max_width, find_chars[-1])
    replace_chars = replace_chars.ljust(max_width, replace_chars[-1])

    trans = str.maketrans(find_chars, replace_chars, "")

    def translator(text: str):
        return text.translate(trans)

    return translator
