from stats import count_words, count_letters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def report(filespec, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {filespec}", filespec)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words") 
    print("--------- Character Count -------")
    sorted_dict = sort_dict(letter_count)
    for item in sorted_dict: 
        if not item[0].isalpha():
            continue
        else:
            print(f"{item[0]}: {item[1]['num']}")
    print("============= END ===============")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        filespec = sys.argv[1]
        text = get_book_text(filespec)
        word_count = count_words(text)
        letter_count = count_letters(text)
        report(filespec, word_count, letter_count)
                
main()
