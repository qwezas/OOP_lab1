import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest

from oop_lab1.TaskPackage2.Task2 import Goods, create_goods


class TestGoods:
    def test_initialization_default(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        assert goods.name == "Test"
        assert goods.registration_date == "2024-01-01"
        assert goods.price == 100.0
        assert goods.amount == 5
        assert goods.invoice_number == "INV001"

    def test_calculate_total_cost(self) -> None:
        goods = Goods("Test", "2024-01-01", 150.0, 3, "INV001")
        assert goods.calculate_total_cost() == 450.0

    def test_calculate_total_cost_zero_amount(self) -> None:
        goods = Goods("Test", "2024-01-01", 150.0, 0, "INV001")
        assert goods.calculate_total_cost() == 0.0

    def test_change_price_valid(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.change_price(200.0)
        assert result is True
        assert goods.price == 200.0

    def test_change_price_invalid(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.change_price(-50.0)
        assert result is False
        assert goods.price == 100.0

    def test_increase_amount_valid(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.increase_amount(3)
        assert result is True
        assert goods.amount == 8

    def test_increase_amount_invalid(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.increase_amount(-1)
        assert result is False
        assert goods.amount == 5

    def test_decrease_amount_valid(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.decrease_amount(3)
        assert result is True
        assert goods.amount == 2

    def test_decrease_amount_invalid_zero(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.decrease_amount(0)
        assert result is False
        assert goods.amount == 5

    def test_decrease_amount_invalid_exceed(self) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        result = goods.decrease_amount(10)
        assert result is False
        assert goods.amount == 5

    def test_display(self, capsys: pytest.CaptureFixture[str]) -> None:
        goods = Goods("Test", "2024-01-01", 100.0, 5, "INV001")
        goods.display()
        captured = capsys.readouterr()
        assert "Наименование товара: Test" in captured.out
        assert "Общая стоимость: 500.0 руб." in captured.out


class TestCreateGoods:
    def test_create_goods_valid(self) -> None:
        goods = create_goods("Test", "2024-01-01", 100.0, 5, "INV001")
        assert isinstance(goods, Goods)
        assert goods.name == "Test"
        assert goods.price == 100.0
        assert goods.amount == 5

    def test_create_goods_negative_price_raises_error(self) -> None:
        with pytest.raises(ValueError):
            create_goods("Test", "2024-01-01", -100.0, 5, "INV001")

    def test_create_goods_negative_amount_raises_error(self) -> None:
        with pytest.raises(ValueError):
            create_goods("Test", "2024-01-01", 100.0, -5, "INV001")

    def test_create_goods_zero_amount(self) -> None:
        goods = create_goods("Test", "2024-01-01", 100.0, 0, "INV001")
        assert goods.amount == 0
