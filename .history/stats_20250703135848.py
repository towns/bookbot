def count_words(text):
    words = text.split()
    return len(words)

def update_dict(dict, key):
    

def count_letters(text):
    dict = {}
    for letter in text:
        key = letter.lower();
        if key in dict:
            dict[key] = {'char': key, 'num': dict[key]['num'] + 1}
        else:
            dict[key] = {'char': key, 'num': 1}
    
    return dict

def sort_on(items):
    return items[1]["num"]

def sort_dict(dict):
    items = list(dict.items())
    items.sort(reverse=True, key=sort_on)
    return items



