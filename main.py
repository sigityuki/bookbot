import sys
from stats import get_num_words, get_num_character, sort_characters

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    word_count = get_num_words(book_contents)
    character_count = get_num_character(book_contents)
    sorted_characters = sort_characters(character_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for character in sorted_characters:
        if character["name"].isalpha():
            print(f"{character["name"]}: {character["count"]}")
    print(f"============= END ===============")

main()
