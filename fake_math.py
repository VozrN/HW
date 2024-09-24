def divide(first, second):
    try:
        result = round(first / second, 2)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:
        print(result)


