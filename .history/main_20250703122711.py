from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    word_count = count_words(get_book_text('books/frankenstein.txt'))
    letter_count = count_letters(get_book_text('books/frankenstein.txt'))
    print(f"{count_words(get_book_text('books/frankenstein.txt'))} words found in the document")
    print(letter_count)    

main()
