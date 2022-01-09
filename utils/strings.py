def is_positive_number(value):
    try:
        number_string = float(value)
    except ValueError:
        return False
    return number_string > 0
