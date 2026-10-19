def parse_positive(text):
    try:
        number = int(text)
    except ValueError:
        raise ValueError("not a positive number")
    if number <= 0:
        raise ValueError("not a positive number")
    return number
