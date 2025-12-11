# Элементы класса, использование ключевого слова self
class River:
    # Список всех рек
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # Добавляем текущую реку в список всех рек
        River.all_rivers.append(self)

    def get_info(self):
        print("Длина реки {0} равна {1} км".format(self.name, self.length))


volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

# Далее печатаем все названия рек
for river in River.all_rivers:
    print(river.name)

# Output:
# Волга
# Сена
# Нил

volga.get_info()
# Длина реки Волга равна 3530 км
seine.get_info()
# Длина реки Сена равна 776 км
nile.get_info()
# Длина реки Нил равна 6852 км
