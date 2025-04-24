check_between_numbers = lambda A, B, C: (A < B < C) or (A > B > C)  # noqa E731


check_odd_three = lambda number: (100 <= abs(number) <= 999) and (  # noqa E731
    number % 2 != 0
)


check_unique_digits = (  # noqa E731
    lambda number: (100 <= abs(number) <= 999)
    and len(set(str(abs(number)))) == 3
)


def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]


check_ascending_digits = lambda number: (100 <= abs(number) <= 999) and (  # noqa E731
    lambda n: n[0] < n[1] < n[2]
)([int(d) for d in str(abs(number))])
