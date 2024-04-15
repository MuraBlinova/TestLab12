import unittest
import math


def сalculator(a, operation, b=1):
    if not isinstance(a, int) and not isinstance(a, float) and not isinstance(b, int) and not isinstance(b,
                                                                                                       float) and operation not in [
        "+", "-", "*", ":", "^", "sqrt", "!"]:
        print("Error: incorrect input")
        return None
    else:
        if operation == "+":
            return a + b
        if operation == "-":
            return a - b
        if operation == "*":
            return a * b
        if operation == ":":
            if b == 0:
                print("Error: division by zero")
                return None
            return a / b
        if operation == "^":
            return a ** b
        if operation == "sqrt":
            if a >= 0:
                return a ** (1 / 2)
            else:
                print("Error: incorrect number")
                return None
        if operation == "!":
            if a % 1 == 0 and a >= 0:
                a = int(a)
                f = 1
                for i in range(a):
                    f *= (i + 1)
                return f
            else:
                print("Error: incorrect number")
                return None


class TestAddNumbers(unittest.TestCase):
    def test_negative_type_input(self):
        result = сalculator("24", 4, True)
        self.assertEqual(result, None)

    def test_add_positive_numbers(self):
        result = сalculator(2, "+", 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = сalculator(-2, "+", -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = сalculator(3, "+", 0)
        self.assertEqual(result, 3)

    def test_subtract_positive_numbers(self):
        result = сalculator(2, "-", 3)
        self.assertEqual(result, -1)

    def test_subtract_negative_numbers(self):
        result = сalculator(-2, "-", -3)
        self.assertEqual(result, 1)

    def test_subtract_zero(self):
        result = сalculator(3, "-", 0)
        self.assertEqual(result, 3)

    def test_multiplication_positive_numbers(self):
        result = сalculator(2, "*", 3)
        self.assertEqual(result, 6)

    def test_multiplication_negative_numbers(self):
        result = сalculator(-2, "*", -3)
        self.assertEqual(result, 6)

    def test_multiplication_diffferent_numbers(self):
        result = сalculator(-2, "*", 3)
        self.assertEqual(result, -6)

    def test_multiplication_zero(self):
        result = сalculator(3, "*", 0)
        self.assertEqual(result, 0)

    def test_multiplication_one(self):
        result = сalculator(3, "*", 1)
        self.assertEqual(result, 3)

    def test_division_positive_numbers(self):
        result = сalculator(6, ":", 3)
        self.assertEqual(result, 2)

    def test_division_negative_numbers(self):
        result = сalculator(-6, ":", -3)
        self.assertEqual(result, 2)

    def test_division_diffferent_numbers(self):
        result = сalculator(-6, ":", 3)
        self.assertEqual(result, -2)

    def test_division_zero(self):
        result = сalculator(3, ":", 0)
        self.assertEqual(result, None)

    def test_division_one(self):
        result = сalculator(3, ":", 1)
        self.assertEqual(result, 3)

    def test_degree_positive_numbers(self):
        result = сalculator(2, "^", 3)
        self.assertEqual(result, 8)

    def test_degree_negative_numbers(self):
        result = сalculator(-2, "^", -2)
        self.assertEqual(result, 0.25)

    def test_degree_different_numbers(self):
        result = сalculator(-2, "^", 3)
        self.assertEqual(result, -8)

    def test_degree_zero(self):
        result = сalculator(3, "^", 0)
        self.assertEqual(result, 1)

    def test_degree_one(self):
        result = сalculator(3, "^", 1)
        self.assertEqual(result, 3)

    def test_sqrt_positive(self):
        result = сalculator(4.0, "sqrt")
        self.assertEqual(result, 2.0)

    def test_sqrt_positive_2(self):
        result = сalculator(0.25, "sqrt", 3)
        self.assertEqual(result, 0.5)

    def test_sqrt_negative(self):
        result = сalculator(-4.0, "sqrt")
        self.assertEqual(result, None)

    def test_factorial_positive(self):
        result = сalculator(4, "!")
        self.assertEqual(result, 24)

    def test_factorial_zero(self):
        result = сalculator(0, "!", 3)
        self.assertEqual(result, 1)

    def test_factorial_negative(self):
        result = сalculator(-4.0, "!")
        self.assertEqual(result, None)

    def test_factorial_float(self):
        result = сalculator(3.0, "!")
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
