def num_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)

def char_num(text):
    """Returns the occurrence of each characters in the given text."""
    char={}
    for c in text:
        c = c.lower()
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
        sort_dict_by_value(char)
    return char

def value_of_dict(d):
    return d["nums"]

def sort_dict_by_value(d):
    list_of_dict = []
    for key, value in d.items():
        list_of_dict.append({"char": key, "nums": value})
        
    list_of_dict.sort(reverse=True, key=lambda x: list(x.values())[0])
    return list_of_dict