calls = 0


def count_calls(num):
    global calls
    calls = calls + 1


def string_info(string):
    count_calls(calls)
    len_1 = len(string)
    upper = string.upper()
    down = string.lower()
    tuple_1 = (len_1, upper, down)
    print(tuple_1)


def is_contains(string, list_to_search):
    count_calls(calls)
    check_string = string.lower() in list_to_search.lower()
    print(check_string)


string = input('Введите одно слово: ')
string_info(string)
string_1 = input('Введите слово из списка: ')
list_to_search = input('Введите список слов: ')
is_contains(string_1, list_to_search)
print(calls)
