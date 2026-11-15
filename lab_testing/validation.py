def check_positive_assert(number):
    assert number > 0, "Число має бути більшим за нуль!"
    return number


def check_positive(number):
    try:
        value = float(number)
    except (TypeError, ValueError):
        raise ValueError("Введіть число, а не текст")
    if value <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return value


def create_name(name):
    if not name:
        raise ValueError("Ім'я не може бути порожнім")
    return name
