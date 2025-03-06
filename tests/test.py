import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_adding_success (self):
        assert self.calc.adding(self, 100, 1) == 101
    def test_subtraction_succes (self):
        assert self.calc.subtraction(self, 90, 49) == 41
    def test_zero_division (self):
        with pytest.raises (ZeroDivisionError):
            self.calc.division (self, 5, 0)
    def test_division_success(self):
        assert self.calc.division(self, 169,13) == 13
    def test_multiply_success (self):
        assert self.calc.multiply(self, 5,6) == 30

    def teardown(self):
        print('Выполнение метода Teardown')