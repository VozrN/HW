import math

math.inf

def divide(first, second):
    try:
        result = round(first / second, 2)
    except ZeroDivisionError:
        print(math.inf)
    else:
        print(result)


