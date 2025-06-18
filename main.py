import sys
from stats import get_num_words, get_freq_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return ""

def analyze(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    content = get_book_text(book)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    freq_char = get_freq_char(content)
    sorted_list = sort_dict(freq_char)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    analyze(sys.argv[1])
    
    


main()
