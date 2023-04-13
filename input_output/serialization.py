from pickle import dump, load


class Toy:
    name = ''
    price = 0.0

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price


t1 = Toy('Potato', 10.5)

f = open('object.bin', 'wb')
dump(t1, f)
f.close()

f = open('object.bin', 'rb')
t2 = load(f)
f.close()

print(type(t2))
print(t2.getName())
