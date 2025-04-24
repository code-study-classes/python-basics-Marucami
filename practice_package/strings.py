extract_file_name = lambda f: (  # noqa E731
    f.replace("\\", "/").split("/")[-1]
    if f.replace("\\", "/").split("/")[-1].startswith(".")
    and f.replace("\\", "/").split("/")[-1].count(".") == 1
    else f.replace("\\", "/").split("/")[-1].split(".")[0]
)


def encrypt_sentence(sentence):
    even_chars = []
    odd_chars = []

    for i, char in enumerate(sentence):
        if i % 2 == 1:
            even_chars.append(char)
        else:
            odd_chars.append(char)

    return "".join(even_chars + odd_chars[::-1])


def check_brackets(expression):
    openCount = 0
    closeCount = 0
    pos = 0
    for i in range(0, len(expression)):
        if expression[i] != ' ':
            pos += 1
        if expression[i] == '(':
            openCount += 1
        elif expression[i] == ')':
            closeCount += 1
        if closeCount > openCount:
            return pos
    if openCount > closeCount:
        return -1
    return 0


def reverse_domain(domain):
    parts = domain.split(".")
    return ".".join(reversed(parts))


def count_vowel_groups(word):
    vowels = {"a", "e", "i", "o", "u", "y"}
    count = 0
    in_vowel_group = False

    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False

    return count
