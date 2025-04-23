calculate_segments = lambda length_a, length_b: length_a // length_b

calculate_segments = lambda length_a, length_b: length_a // length_b

calculate_digit_sum = lambda number: sum(int(digit) for digit in str(abs(number)))

def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple


def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height