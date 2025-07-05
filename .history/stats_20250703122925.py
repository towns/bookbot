def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter_to_check = letter.lower();
        if letter_to_check in letters:
            letters[letter_to_check] += 1
        else:
            letters[letter_to_check] = 1
    return letters
