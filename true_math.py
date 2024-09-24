import math

from math import inf

def divide(first, second):
    try:
        result = round(first / second, 2)
    except ZeroDivisionError:
        return inf
    else:
        return result


