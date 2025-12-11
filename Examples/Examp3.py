# Использование свойств
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height


# Работа с width и height как будто они являются атрибутами
rect = Rectangle(10, 20)

rect.width = 50
rect.height = 70

print(rect.width)
# 50
print(rect.height)
# 70
rect.width = -10
# Выдаст ошибку, так как в сеттере указали условие > 0
