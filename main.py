from stats import number_of_words
from stats import get_character_count
from stats import sort_dict
import sys

def get_book_text(file_path):
    string = ""
    with open(file_path) as f:
        string = f.read()
    return string

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    string = get_book_text(sys.argv[1])
    num_words = number_of_words(string)
    num_chars = get_character_count(string)
    sorted_dict = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # e: 44538
    for dict in sorted_dict:
        if dict["name"].isalpha() :
            print(f"{dict["name"]}: {dict["num"]}")



main()