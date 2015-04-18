import unittest
from the_real_deal import sum_of_divisors
from the_real_deal import is_prime
from the_real_deal import prime_number_of_divisons
from the_real_deal import contains_digit
from the_real_deal import contains_digits
from the_real_deal import is_number_balanced
from the_real_deal import count_substrings
from the_real_deal import zero_insertion
from the_real_deal import sum_matrix
from the_real_deal import matrix_bombing_plan


class TestRealDeal(unittest.TestCase):

    def test_sum_of_divisiors(self):
        self.assertEqual(sum_of_divisors(8), 15)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-10))

    def test_prime_number_of_divisons(self):
        self.assertFalse(prime_number_of_divisons(8))
        self.assertTrue(prime_number_of_divisons(7))

    def test_contains_digit(self):
        self.assertFalse(contains_digit(123, 4))
        self.assertTrue(contains_digit(42, 2))

    def test_contains_digits(self):
        self.assertFalse(contains_digits(123, [4, 1]))
        self.assertTrue(contains_digits(123, [1, 3]))

    def test_is_number_balanced(self):
        self.assertFalse(is_number_balanced(13))
        self.assertTrue(is_number_balanced(4518))

    def test_count_substrings(self):
        self.assertEqual(
            count_substrings("This is this and that is this", "this"), 2)

    def test_zero_insertion(self):
        self.assertEqual(zero_insertion(6446), 6040406)

    def test_sum_matrix(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_matrix(m), 45)

    def test_matrix_bombing_plan(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        needed_answer = {(0, 0): 42,
                         (0, 1): 36,
                         (0, 2): 37,
                         (1, 0): 30,
                         (1, 1): 15,
                         (1, 2): 23,
                         (2, 0): 29,
                         (2, 1): 15,
                         (2, 2): 26}
        self.assertEqual(matrix_bombing_plan(m), needed_answer)

if __name__ == "__main__":
    unittest.main()
