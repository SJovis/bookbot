from stats import get_num_words, get_num_char

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()
        return content

def main():
    content = get_book_text('./books/frankenstein.txt')
    words_count = get_num_words(content)
    chars_count = get_num_char(content)
    print(f'{len(words_count)} words found in the document.')
    print(chars_count)
main()
