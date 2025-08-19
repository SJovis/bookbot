from stats import get_num_words, get_num_char, sort_dicts

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()
        return content

def show_list(content: list):
    for dict in content:
        print(f'{dict['char']}: {dict['num']}')

def main():
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at books/frankenstein.txt...')
    content = get_book_text('./books/frankenstein.txt')
    print('----------- Word Count ----------')
    words_count = get_num_words(content)
    print(f'Found {len(words_count)} total words')
    print('--------- Character Count -------')
    chars_count = get_num_char(content)
    sorted_list = sort_dicts(chars_count)
    show_list(sorted_list)
    print('============= END ===============')
main()
