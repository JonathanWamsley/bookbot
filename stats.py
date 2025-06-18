def get_num_words(text):
    words = text.split()
    return len(words)

def get_freq_char(text):
    freq_count = {}
    for char in text.lower():
        if char not in freq_count:
            freq_count[char] = 0
        freq_count[char] +=1
    return freq_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        dict_list.append(
            {"char": key, "num": dict[key]}
        )
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
