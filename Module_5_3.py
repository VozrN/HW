class House:
    def __init__(self, n, fl):
        self.name = n
        self.number_of_floors = fl

    def go_to(self, new_flow):
        if new_flow > self.number_of_floors or new_flow < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_flow + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название:' + self.name + ', количество этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError('Число этажей должно быть целым числом')
        oth = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors == oth

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
