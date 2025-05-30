def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    return (
        amount / 10 if amount >= 5000 else amount / 20 if amount >= 1000 else 0
    )


def describe_number(n):
    even = "четное" if n % 2 == 0 else "нечетное"

    if 0 <= n <= 9:
        digit = "однозначное"
    elif 10 <= n <= 99:
        digit = "двузначное"
    else:
        digit = "трехзначное"

    return f"{even} {digit} число"


def convert_to_meters(unitNumber, lengthInUnits):
    conversion = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01,
    }
    return lengthInUnits * conversion.get(unitNumber, 1)


def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто",
    }

    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
    }

    if age % 10 == 0:
        word = tens[age // 10]
        suffix = "лет"
    else:
        word = f"{tens[age // 10]} {units[age % 10]}"
        last_digit = age % 10
        suffix = (
            "год"
            if last_digit == 1
            else "года"
            if 2 <= last_digit <= 4
            else "лет"
        )

    return f"{word} {suffix}"
