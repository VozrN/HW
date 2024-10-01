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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
