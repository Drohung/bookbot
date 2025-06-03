def count_words(book_contents):
    book_words_list = book_contents.split()
    book_word_count = len(book_words_list)
    return book_word_count

def character_count(book_contents):
    lower_string = book_contents.lower()
    char_list = list(lower_string)
    char_dict = {}

    for letter in char_list:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict

def dictionary_list(character_dictionary):
    dict_list = []

    for k,v in character_dictionary.items():
        dict_entry = {
            "name": k,
            "num": v,
        }
        dict_list.append(dict_entry)
    dict_list.sort(reverse=True, key=sort_by)
    return dict_list

def sort_by(dict):
    return dict["num"]



