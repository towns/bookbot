def count_words(text):
    words = text.split()
    return len(words)

def update_dict(dict, key):
    #print(f"Updating dict with {key}")

    if(dict[key] != None):
        dict[key] = {'char': key, 'num': dict[key]['num'] + 1}
    else:
        dict[key] = {'char': key, 'num': 1}

def count_letters(text):
    letter_count_dict = {}

    for letter in text:
        update_dict(letter_count_dict, letter.lower())

    print(f"list: {letter_count_dict}")
    return letter_count_dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sorted = dict.sort(reverse=True, key=sort_on)
    print(sorted)



