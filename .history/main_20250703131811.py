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

    print("about to sort")
    
    sorted_dict = sort_dict(letter_count)
    print(sorted)
    

def main():
    filespec = 'books/frankenstein.txt'
    word_count = count_words(get_book_text('books/frankenstein.txt'))
    letter_count = count_letters(get_book_text('books/frankenstein.txt'))
    report(filespec, word_count, letter_count)


main()
