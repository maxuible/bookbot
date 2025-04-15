

def number_of_words(string):
    return len(string.split())

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    list = []
    for entry in dictionary:
        list.append(
            {"name": entry, "num": dictionary[entry]}
            )
    list.sort(reverse=True, key=sort_on)
    return list


def get_character_count(string):
    dict = {}
    for s in string.lower():
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    return dict