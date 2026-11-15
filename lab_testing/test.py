import unittest
from unittest.mock import patch

from validation import check_positive, check_positive_assert, create_name
from text_utils import count_symbols, count_vowels, divide
from app import Figure
from input_app import ask_number


class TestValidation(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(5.0, check_positive("5"))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            check_positive("-3")

    def test_text_instead_of_number(self):
        with self.assertRaises(ValueError):
            check_positive("abc")

    def test_assert_fails(self):
        with self.assertRaises(AssertionError):
            check_positive_assert(-1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            create_name("")


class TestTextUtils(unittest.TestCase):
    def test_count_symbols(self):
        self.assertEqual(3, count_symbols("abc"))
        self.assertEqual(0, count_symbols(""))

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_vowels_basic(self):
        self.assertEqual(2, count_vowels("hello"))

    def test_vowels_none(self):
        self.assertEqual(0, count_vowels("bcd"))

    def test_vowels_upper(self):
        self.assertEqual(3, count_vowels("AEI"))

    def test_vowels_empty(self):
        self.assertEqual(0, count_vowels(""))

    def test_vowels_digits(self):
        self.assertEqual(0, count_vowels("12345"))
        self.assertEqual(1, count_vowels("a12345"))

    def test_vowels_ukrainian(self):
        self.assertEqual(2, count_vowels("Привіт"))
        self.assertEqual(4, count_vowels("Україна"))


class TestFigure(unittest.TestCase):
    def setUp(self):
        self.square = Figure("квадрат", 4)

    def test_type(self):
        self.assertEqual("квадрат", self.square.get_figure_type)

    def test_length(self):
        self.assertEqual(4, self.square.get_figure_length)

    def test_figure_lengths(self):
        for length in [1, 5, 10]:
            with self.subTest(length=length):
                self.assertEqual(length, Figure("квадрат", length).get_figure_length)

    def test_all_types_subtest(self):
        for t in ["квадрат", "прямокутник", "трикутник"]:
            with self.subTest(figure_type=t):
                self.assertEqual(t, Figure(t, 2).get_figure_type)

    def test_angles(self):
        self.assertEqual([90] * 4, Figure("квадрат", 1).get_angles())
        self.assertEqual([90] * 4, Figure("прямокутник", 1).get_angles())
        self.assertEqual([60] * 3, Figure("трикутник", 1).get_angles())

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", -5)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            Figure("коло", 3)


class TestInput(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_ask_number(self, mock_input):
        self.assertEqual(10, ask_number())
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main()
