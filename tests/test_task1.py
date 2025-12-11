import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from oop_lab1.TaskPackage1.Task1 import Pair, make_pair


class TestPair:
    def test_initialization_default(self) -> None:
        pair = Pair()
        assert pair.first == 1.0
        assert pair.second == 1.0

    def test_initialization_with_values(self) -> None:
        pair = Pair(3.0, 4.0)
        assert pair.first == 3.0
        assert pair.second == 4.0

    def test_initialization_negative_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Pair(-1.0, 2.0)

    def test_hypotenuse_calculation(self) -> None:
        pair = Pair(3.0, 4.0)
        assert math.isclose(pair.hypotenuse(), 5.0)

    def test_hypotenuse_zero(self) -> None:
        pair = Pair(0.0, 0.0)
        assert pair.hypotenuse() == 0.0

    def test_display(self, capsys: pytest.CaptureFixture[str]) -> None:
        pair = Pair(3.5, 4.2)
        pair.display()
        captured = capsys.readouterr()
        assert "a = 3.5, b = 4.2" in captured.out

    def test_read_method_not_tested(self) -> None:
        pass


class TestMakePair:
    def test_make_pair_positive(self) -> None:
        pair = make_pair(3.0, 4.0)
        assert isinstance(pair, Pair)
        assert pair.first == 3.0
        assert pair.second == 4.0

    def test_make_pair_negative_raises_error(self) -> None:
        with pytest.raises(ValueError):
            make_pair(-1.0, 2.0)
