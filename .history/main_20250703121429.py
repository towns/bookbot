def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
