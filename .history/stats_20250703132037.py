def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count_dict = []

    for letter in text:
        print("here")
        letter_to_check = letter.lower();

        for entry in letter_count_dict:
            if entry['char'] == letter_to_check:
                entry['num'] += 1   
                print(f"Updating count for {letter_to_check} to {entry['num']}")
        else:
            print(f"Adding {letter_to_check} to the list")
            letter_count_dict.append({'char': letter_to_check, 'num': 1})
    
    print("done")
    return letter_count_dict

def sort_on(items):
    return items["num"]

def sort_dict(letter_dict):
    sorted = letter_dict.sort(reverse=True, key=sort_on)
    print(sorted)



