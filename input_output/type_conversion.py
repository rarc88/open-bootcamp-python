num = 511
print(type(num))

numStr = str(num)
print(type(numStr))

print()


class Toy:
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # overload
    def __str__(self):
        return f'My name is {self.name} and my price is {self.price}'

    def __repr__(self):
        return f'Toy({self.name, self.price})'


t1 = Toy('Potato', 10.5)
print(t1)
print(str(t1))
print(repr(t1))
