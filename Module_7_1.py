class Product:
    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        information_about_product = self.name + ', ' + str(self.weight) + ', ' + self.category
        return information_about_product


class Shop:
    def get_products(self):
        file = open('products.txt', 'r')
        read_file = file.read()
        file.close()
        return read_file

    def add(self, *products):
        for i in products:
            if str(i) not in self.get_products():
                file = open('products.txt', 'a')
                file.write(str(i) + '\n')
                file.close()
            else:
                print(f'Продукт {i} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
