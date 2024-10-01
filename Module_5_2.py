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
        return 'Название:'+self.name+', количество этажей: '+str(self.number_of_floors)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
