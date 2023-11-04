from unittest import TestCase
import mathematics


class TestMathematics(TestCase):
    def test_add(self):
        result = mathematics.add(1, 1)
        self.assertEqual(result, 2)

    def test_subtract(self):
        result = mathematics.subtract(1, 1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = mathematics.multiply(1, 1)
        self.assertEqual(result, 1)

    def test_divide(self):
        result = mathematics.divide(1, 1)
        self.assertEqual(result, 1)

    def test_modulus(self):
        result = mathematics.modulus(1, 1)
        self.assertEqual(result, 0)

    def test_power(self):
        result = mathematics.power(1, 1)
        self.assertEqual(result, 1)
