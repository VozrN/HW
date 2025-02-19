
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin) and self.__is_valid_numbers(__numbers):
            self.__vin = __vin
            self.__numbers = __numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if vin_number < 1000000 or vin_number > 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return vin_number
        raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return numbers
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        raise IncorrectCarNumbers('Некорректный тип данных для номеров')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
