def count_words(text):
    words = text.split()
    return len(words)

def update_dict(dict, key):
    #print(f"Updating dict with {key}")

    if key in dict:
        dict[key] = {'char': key, 'num': dict[key]['num'] + 1}
    else:
        dict[key] = {'char': key, 'num': 1}

def count_letters(text):
    letter_count_dict = {}

    for letter in text:
        update_dict(letter_count_dict, letter.lower())
    return letter_count_dict

def sort_on(items):
    return items[1]["num"]

def sort_dict(dict):
    items = list(dict.items())
    items.sort(reverse=True, key=sort_on)

    return items



