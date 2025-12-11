class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width: float = width
        self.__height: float = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, w: float) -> None:
        if w > 0:
            self.__width = w
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, h: float) -> None:
        if h > 0:
            self.__height = h
        else:
            raise ValueError("Height must be positive")

    def area(self) -> float:
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
