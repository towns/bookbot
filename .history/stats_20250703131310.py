def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count_dict = []

    for letter in text:
        letter_to_check = letter.lower();

        for entry in letter_count_dict:
            if entry['char'] == letter_to_check:
                entry['num'] += 1   
                break
        else:
            letter_count_dict.append({'char': letter_to_check, 'num': 1})
    return letter_count_dict

def sort_on(items):
    return items["num"]


def sort_dict(letter_dict):
    return letter_dict.sort(reverse=True, key=sort_on)



