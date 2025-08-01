from stats import count_words, count_letters, sort_dict

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
    filespec = 'books/frankenstein.txt'
    text = get_book_text('books/frankenstein.txt')
    word_count = count_words(text)
    letter_count = count_letters(text)
    report(filespec, word_count, letter_count)


main()
