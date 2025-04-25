def sum_even_digits(number):
    number = abs(number)
    total = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total


def count_vowel_triplets(text):
    vowels = {"a", "e", "i", "o", "u", "y"}
    count = 0
    text = text.lower()
    i = 0
    while i < len(text) - 2:
        if all(c in vowels for c in text[i : i + 3]):
            count += 1
            i += 3
        else:
            i += 1
    return count


def find_fibonacci_index(number):
    a, b = 0, 1
    index = 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return string
    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)
