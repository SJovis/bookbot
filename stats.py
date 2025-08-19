def get_num_words(content: str):
    words: list[str] = content.split()
    return words

def get_num_char(content: str):
    words: list[str] = content.split()
    chars: dict[str, int] = {}
    for word in words:
        for c in word:
            chars[c.lower()] = chars.get(c.lower(),0) + 1
    return chars
    
