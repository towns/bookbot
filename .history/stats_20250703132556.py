def count_words(text):
    words = text.split()
    return len(words)

def update_dict(dict, key):
    for entry in dict:
        if entry['char'] == key:
            entry['num'] += 1   
            print(f"Updating count for {key} to {entry['num']}")
        else:
            print(f"Adding {key} to the list")
            dict.append({'char': key, 'num': 1})



def count_letters(text):
    letter_count_dict = []

    for letter in text:
        letter_to_check = letter.lower();
        update_dict(letter_count_dict, letter_to_check)
        
    print("done")
    return letter_count_dict

def sort_on(items):
    return items["num"]

def sort_dict(letter_dict):
    sorted = letter_dict.sort(reverse=True, key=sort_on)
    print(sorted)



