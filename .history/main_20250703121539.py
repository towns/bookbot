def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")
main()
