from typing import Self


class Goods:
    def __init__(
        self,
        name: str,
        registration_date: str,
        price: float,
        amount: int,
        invoice_number: str,
    ) -> None:
        self.name: str = name
        self.registration_date: str = registration_date
        self.price: float = price
        self.amount: int = amount
        self.invoice_number: str = invoice_number

    def read(self) -> None:
        self.name = input("Введите наименование товара: ")
        self.registration_date = input("Введите дату оформления: ")

        price_input = input("Введите цену товара: ")
        self.price = float(price_input)
        if self.price < 0:
            raise ValueError("Цена не может быть отрицательной")

        amount_input = input("Введите количество единиц товара: ")
        self.amount = int(amount_input)
        if self.amount < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.invoice_number = input("Введите номер накладной: ")

    def display(self) -> None:
        print(f"Наименование товара: {self.name}")
        print(f"Дата оформления: {self.registration_date}")
        print(f"Цена товара: {self.price} руб.")
        print(f"Количество единиц: {self.amount}")
        print(f"Номер накладной: {self.invoice_number}")
        print(f"Общая стоимость: {self.calculate_total_cost()} руб.")

    def change_price(self, new_price: float) -> bool:
        if new_price < 0:
            print("Цена не может быть отрицательной")
            return False

        old_price: float = self.price
        self.price = new_price
        print(f"Цена товара '{self.name}' изменена с {old_price} на {new_price}")
        return True

    def increase_amount(self, increment: int) -> bool:
        if increment <= 0:
            print("Ошибка: количество для увеличения должно быть положительным")
            return False

        old_amount: int = self.amount
        self.amount += increment
        print(
            f"Количество товара '{self.name}' увеличено с {old_amount} до {self.amount}"
        )
        return True

    def decrease_amount(self, decrement: int) -> bool:
        if decrement <= 0:
            print("Ошибка: количество для уменьшения должно быть положительным")
            return False

        if decrement > self.amount:
            print(
                f"Ошибка: невозможно уменьшить на {decrement}, доступно только {self.amount} единиц"
            )
            return False

        old_amount: int = self.amount
        self.amount -= decrement
        print(
            f"Количество товара '{self.name}' уменьшено с {old_amount} до {self.amount}"
        )
        return True

    def calculate_total_cost(self) -> float:
        return self.price * self.amount


def create_goods(
    name: str, registration_date: str, price: float, quantity: int, invoice_number: str
) -> Goods:
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")

    return Goods(name, registration_date, price, quantity, invoice_number)


if __name__ == "__main__":
    print("Создание объекта, вывод данных о товаре с помощью display():")
    product1 = Goods("Ноутбук", "15.01.2024", 50000, 10, "001")
    product1.display()

    print("Изменение цены товара:")
    product1.change_price(48990)

    print("Увеличение количества товара на 12 единиц:")
    product1.increase_amount(12)

    print("Уменьшение количества товара на 15 единиц:")
    product1.decrease_amount(15)

    print(
        "Вывод уведомления о том, что количество товара меньше числа уменьшения количества (попытка уменьшить на 100):"
    )
    product1.decrease_amount(100)

    print("Возврат общей суммы всех товаров на складе:")
    print(
        f"Общая сумма товара {product1.name}: {product1.calculate_total_cost()} рублей"
    )
