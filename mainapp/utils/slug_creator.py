def create_slug(string):
    alphabet = {'а': 'a', "б": 'b', "в": 'v', "г": 'g', "д": 'd', "е": 'e', "ё": 'ie', "ж": 'ge',
                "з": 'z', "и": 'i', "й": 'io', "к": 'k', "л": 'l', "м": 'm', "н": 'n', "о": 'o',
                "п": 'p', "р": 'r', "с": 's', "т": 't', "у": 'y', "ф": 'f', "х": 'h', "ц": 'ce',
                "ч": '4', "ш": '6', "щ": 'c4a', "ъ": '', "ы": '', "ь": '', "э": 'e',
                "ю": 'iy', "я": 'ia', ' ': '-', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                '6': '6', '7': '7', '8': '8', '9': '9', '0': '0'}
    slug = ''.join([alphabet[letter] for letter in string])
    return slug
