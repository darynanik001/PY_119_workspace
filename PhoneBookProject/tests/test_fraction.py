from PhoneBookProject.fraction.fraction import Fraction
import unittest


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.fraction1 = Fraction(1, 2)
        self.fraction2 = Fraction(2, 3)
        self.fraction3 = Fraction(0, 0)
        self.fraction4 = Fraction(1, 2)

    def test_add(self):
        res = self.fraction1 + self.fraction2
        self.assertEqual(res, Fraction(3, 5),
                         "Fraction(1, 2) + Fraction(2, 3) not equal to Fraction(3, 5)")

    def test_subtract(self):
        res = self.fraction1 - self.fraction2
        self.assertEqual(res, Fraction(-1, -1),
                         "Fraction(1, 2) - Fraction(2, 3) not equal to Fraction(-1, -1)")

    def test_multiply(self):
        res = self.fraction1 * self.fraction2
        self.assertEqual(res, Fraction(2, 6),
                         "Fraction(1, 2) * Fraction(2, 3) not equal to Fraction(2, 6)")

    def test_divide_by_non_zero_number(self):
        res = self.fraction1 / self.fraction2

        self.assertEqual(res, Fraction(1 / 2, 2 / 3),
                         "Fraction(1, 2) / Fraction(2, 3) not equal to Fraction(0, 0)")

    def test_divide_by_zero_number(self):
        message = self.fraction1 / self.fraction3
        self.assertEqual(message, "Division by 0 is not allowed.",
                         "message is not equal to 'Division by 0 is not allowed.'")

    def test_equals(self):
        is_equal = self.fraction1 == self.fraction4
        self.assertTrue(is_equal, True)

    def test_not_equals(self):
        is_not_equal = self.fraction1 == self.fraction2
        self.assertTrue(is_not_equal, False)


if __name__ == '__main__':
    unittest.main()
