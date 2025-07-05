print("greetings boots")

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
   
def main():
    print(get_book_text("books/frankenstein.txt"))

main()
