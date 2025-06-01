import unittest
from src.application.calculator import Calculator

# python3 -m unittest -v

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_implicit_operations(self):
        self.assertEqual(self.calculator.compute("3(5)"), 15)
        self.assertEqual(self.calculator.compute("(2+3)(4+1)"), 25)
        self.assertEqual(self.calculator.compute("6 + (3+1)(2+2)"), 22)
        self.assertEqual(self.calculator.compute("3+3(5)"), 18)
        self.assertEqual(self.calculator.compute("(5)3+3"), 18)

    def test_simple_operations(self):
        self.assertEqual(self.calculator.compute("2+2*4"), 10)
        self.assertEqual(self.calculator.compute("(2+2)4"), 16)
    
    def test_complex_operations(self):
        self.assertEqual(self.calculator.compute("2 + 4 * 10 ^ 2 / 16 - 3"), 24)
        self.assertEqual(self.calculator.compute("(2 + 1) * (8 / 2) / (18 * 2)"), 0.3333333333333333)
        self.assertEqual(self.calculator.compute("(2 + (4 - 3)) * (10 / 5)"), 6)
    
    def test_nested_expressions(self):
        self.assertAlmostEqual(
            self.calculator.compute("((15 * 2^3 - (48 / 6 + 2^2)) * 3) / ((100 / 25 * 3) + (7^2 - 40))"),
            15.428,
            places=2
        )
        self.assertEqual(
            self.calculator.compute("(((3 + 5) * (2 - 1)) + ((6 / 2) ^ 2)) * (4 + 1)"),
            85
        )
        self.assertEqual(
            self.calculator.compute("(((((1 + 2) * 3) + 4) * (5 + (6 - 2))) ^ 2)"),
            13689
        )
    
    def test_power_operations(self):
        self.assertEqual(
            self.calculator.compute("((2^3^2) + ((4 + 1) * (6 - 2))) / ((7 + 3) * (2 + 2))"),
            13.3
        )
    
    def test_large_calculations(self):
        self.assertEqual(
            self.calculator.compute("((((1 + 2) + 3) + 4) + 5) * (((6 * 7) * 8) * 9)"),
            45360
        )
        self.assertEqual(
            self.calculator.compute("(((((10 - 2)^2) + ((3 + 1)^3)) * ((8 / 4)^2)))"),
            512
        )
        self.assertEqual(
            self.calculator.compute("(((((1+2)*(3+4))-((5+6)*(7+8)))+((9+10)*(11+12)))^2)"),
            85849
        )

if __name__ == "__main__":
    unittest.main()