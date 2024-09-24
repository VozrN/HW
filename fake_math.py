def divide(first, second):
    try:
        result = round(first / second, 2)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    else:
        return result


