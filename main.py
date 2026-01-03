import sys
from stats import num_words, char_num
def get_book_text(file_path):
    """Reads the content of a text file and returns it as a string."""
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = num_words(book_text)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    char_count = char_num(book_text)
    for key, value in char_count.items():
        print(f"{key}: {value}")
if __name__ == "__main__":  
    main()
