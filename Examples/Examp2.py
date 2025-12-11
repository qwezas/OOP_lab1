# Создание атрибутов с помощью методов
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))

    # Изменение атрибутов с помощью методов
    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("cannot unload that much")


black_pearl = Ship("Black Pearl", 800)
black_pearl.name_captain("Jack Sparrow")
# Печатает "Jack Sparrow is the captain of the Black Реагl"

print(black_pearl.captain)
# Печатает "Jack Sparrow"

black_pearl.load_cargo(600)
# "Loaded 600 tons"
# cargo = 600

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"
# cargo = 200

black_pearl.load_cargo(700)
# "Cannot load that much"
# cargo = 200

black_pearl.unload_cargo(300)
# "Cannot unload that much"
# cargo = 200
