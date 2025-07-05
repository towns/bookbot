from stats import count_words

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    print(f"{count_words(get_book_text('books/frankenstein.txt'))} words found in the document")
main()
