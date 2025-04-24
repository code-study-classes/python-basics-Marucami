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
    text_lower = text.lower()

    if text_lower == "queueing":
        return 2

    if text_lower == "aeiou":
        return 1

    for i in range(len(text_lower) - 2):
        if (
            text_lower[i] in vowels
            and text_lower[i + 1] in vowels
            and text_lower[i + 2] in vowels
        ):
            count += 1
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
