def count_char_occurrences(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted


def dict_to_table():
    pass


def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result:
            if isinstance(value, dict) and isinstance(result[key], dict):
                result[key] = deep_update(result[key], value)
            else:
                result[key] = value
    return result
