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

def sort_by_count(item: dict):
    return item['num']


def sort_dicts(data: dict) -> list :
    sorted_list: list[dict] = []
    for k, v in data.items():
        sorted_list.append({'char': k, 'num': v})
    sorted_list.sort(reverse=True, key=sort_by_count)
    return sorted_list

 
