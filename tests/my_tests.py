from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_umnojenie_correct(self):
        assert self.calculator.umnojenie(self, 2, 3) == 6

    def test_delenie_correct(self):
        assert self.calculator.delenie(self, 9, 3) == 3

    def test_slojenie_positive(self):
        assert self.calculator.slojenie(self, 3, 1) == 4

    def test_vichetanie_positive(self):
        assert self.calculator.raznost(self, 6, 4) == 2

    def test_stepeni_positive(self):
        assert self.calculator.stepen(self, 4, 2) == 16


