import unittest
from histogramClass import Histogram


class TestHistogram(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()

    def test_init(self):
        self.assertIsInstance(self.h, Histogram)

    def test_add(self):
        self.assertFalse(self.h.add("Blaa"))
        self.h.add("nginx")
        self.h.add("nginx")
        needed = {"nginx": 2}
        self.assertEqual(needed, self.h.my_dict)

    def test_count(self):
        self.h.add("nginx")
        self.h.add("nginx")
        self.assertEqual(2, self.h.count("nginx"))
        self.assertEqual(None, self.h.count("Blal"))

    def test_str(self):
        pass

    def test_get_dict(self):
        self.assertEqual(self.h.my_dict, self.h.get_dict())

if __name__ == "__main__":
    unittest.main()
