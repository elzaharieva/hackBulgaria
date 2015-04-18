import unittest
from warmup import fibonacci
from warmup import factorial
from warmup import fact_digits
from warmup import sum_of_digits
from warmup import palindrome
from warmup import to_digits
from warmup import to_number
from warmup import fib_number
from warmup import count_vowels
from warmup import count_consonants
from warmup import char_histogram
from warmup import p_score
from warmup import is_increasing
from warmup import is_decreasing
from warmup import next_hack


class TestWarmups(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(5), [1, 1, 2, 3, 5])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fact_digits(self):
        self.assertEqual(fact_digits(52), 122)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(152), 8)

    def test_palindrome(self):
        self.assertFalse(palindrome("baba"))
        self.assertTrue(palindrome("ABBA"))

    def test_to_digits(self):
        self.assertEqual(to_digits(123), [1, 2, 3])

    def test_to_number(self):
        self.assertEqual(to_number([1, 2, 2]), 122)

    def test_fib_number(self):
        self.assertEqual(fib_number(10), 11235813213455)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)

    def test_char_histogram(self):
        self.assertEqual(
            char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})

    def test_p_score(self):
        self.assertEqual(p_score(198), 6)

    def test_is_increasing(self):
        self.assertFalse(is_increasing([1, 2, 1]))
        self.assertTrue(is_increasing([1, 2, 3]))

    def test_is_decreasing(self):
        self.assertFalse(is_decreasing([1, 2, 1]))
        self.assertFalse(is_decreasing([1, 2, 3]))
        self.assertTrue(is_decreasing([4, 2]))

    def test_next_hack(self):
        self.assertEqual(next_hack(8031), 8191)

if __name__ == "__main__":
    unittest.main()
