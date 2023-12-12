import unittest
from stats import (calculate_mean, calculate_median, calculate_mode,
                          calculate_range, sort_numbers, filter_even_numbers,
                          filter_odd_numbers, find_max, find_min, calculate_sum,
                          count_occurrences, reverse_list, is_palindrome,
                          square_numbers, cube_numbers, find_primes)

class TestNumberFunctions(unittest.TestCase):
    def setUp(self):
        self.numbers = [12, 34, 56, 23, 45, 67, 89, 10, 5, 43]

    def test_calculate_mean(self):
        self.assertEqual(calculate_mean(self.numbers), 38.4)

    def test_calculate_median(self):
        self.assertEqual(calculate_median(self.numbers), 38.5)

    def test_calculate_mode(self):
        self.assertEqual(calculate_mode(self.numbers), None)  # No unique mode

    def test_calculate_range(self):
        self.assertEqual(calculate_range(self.numbers), 84)

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers(self.numbers), [5, 10, 12, 23, 34, 43, 45, 56, 67, 89])

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers(self.numbers), [12, 34, 56, 10])

    def test_filter_odd_numbers(self):
        self.assertEqual(filter_odd_numbers(self.numbers), [23, 45, 67, 89, 5, 43])

    def test_find_max(self):
        self.assertEqual(find_max(self.numbers), 89)

    def test_find_min(self):
        self.assertEqual(find_min(self.numbers), 5)

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(self.numbers), 384)

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences(self.numbers, 10), 1)

    def test_reverse_list(self):
        self.assertEqual(reverse_list(self.numbers), [43, 5, 10, 89, 67, 45, 23, 56, 34, 12])

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(self.numbers))
        palindrome_list = [1, 2, 3, 2, 1]
        self.assertTrue(is_palindrome(palindrome_list))

    def test_square_numbers(self):
        self.assertEqual(square_numbers(self.numbers), [144, 1156, 3136, 529, 2025, 4489, 7921, 100, 25, 1849])

    def test_cube_numbers(self):
        self.assertEqual(cube_numbers(self.numbers), [1728, 39304, 175616, 12167, 91125, 300763, 704969, 1000, 125, 79507])

    def test_find_primes(self):
        self.assertEqual(find_primes(self.numbers), [23, 67, 89, 5, 43])

if __name__ == "__main__":
    unittest.main()
