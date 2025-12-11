from TaskPackage1.Task1 import Pair


def main() -> None:
    print("Создание объекта, передача значений с помощью аргументов:")
    p1 = Pair(3.0, 4.0)
    p1.display()

    print("Вывод гипотенузы на экран:")
    print(f"Гипотенуза = {p1.hypotenuse()}")

    print("Создание объекта, передача значений с помощью метода read():")
    p2 = Pair()
    p2.read()
    p2.display()
    print(f"Гипотенуза = {p2.hypotenuse()}")

    print(
        "Создание объекта, передача значений с помощью аргументов и вывод на экран полей dispay():"
    )
    p3 = Pair(3.0, 4.0)
    p3.display()


if __name__ == "__main__":
    main()
