def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter_to_check = letter.lower();
        entry = letters[letter_to_check] 
        if letters[letter_to_check] is None:
            letters[letter_to_check] = 1
        else:
            letters[letter_to_check] += 1
    return letters
