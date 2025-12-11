import math
from typing import Self


class Pair:
    def __init__(self, first: float = 1.0, second: float = 1.0) -> None:
        if first < 0 or second < 0:
            raise ValueError("Числа должны быть положительными.")

        self.first: float = first
        self.second: float = second

    def read(self) -> None:
        first_input: float = float(input("Введите сторону a: "))
        second_input: float = float(input("Введите сторону b: "))

        if first_input < 0 or second_input < 0:
            raise ValueError("Числа должны быть положительными.")
        self.first = first_input
        self.second = second_input

    def display(self) -> None:
        print(f"a = {self.first}, b = {self.second}")

    def hypotenuse(self) -> float:
        return math.sqrt(self.first**2 + self.second**2)


def make_pair(first: float, second: float) -> Pair:
    return Pair(first, second)


if __name__ == "__main__":
    print(
        "Создание объекта с помощью функции make_pair(), передача значений с помощью аргументов:"
    )
    p1 = make_pair(3, 4)
    p1.display()

    print("Вывод гипотенузы на экран:")
    print(f"Гипотенуза = {p1.hypotenuse()}")

    print(
        "Создание объекта без функции make_pair(), передача значений с помощью метода read():"
    )
    p2 = Pair()
    p2.read()
    p2.display()
    print(f"Гипотенуза = {p2.hypotenuse()}")

    print(
        "Создание объекта, передача значений с помощью аргументов и вывод на экран полей dispay():"
    )
    p3 = Pair(3, 4)
    p3.display()

    print("Проверка работы обработчика ошибок, передача отрицательных значений")
    p4 = make_pair(-1, 4)  # Ошибка создания объекта: Числа должны быть положительными.
