from TaskPackage2.Task2 import Goods


def main() -> None:
    print("Создание объекта, вывод данных о товаре с помощью display():")
    product1 = Goods("Ноутбук", "15.01.2024", 50000.0, 10, "001")
    product1.display()

    print("Изменение цены товара:")
    product1.change_price(48990.0)

    print("Увеличение количества товара на 12 единиц:")
    product1.increase_amount(12)

    print("Уменьшение количества товара на 15 единиц:")
    product1.decrease_amount(15)

    print(
        "Вывод уведомления о том, что количество товара меньше числа уменьшения количества (попытка уменьшить на 100):"
    )
    print("меньше числа уменьшения количества (попытка уменьшить на 100):")
    product1.decrease_amount(100)

    print("Возврат общей суммы всех товаров на складе:")
    print(
        f"Общая сумма товара {product1.name}: {product1.calculate_total_cost()} рублей"
    )


if __name__ == "__main__":
    main()
