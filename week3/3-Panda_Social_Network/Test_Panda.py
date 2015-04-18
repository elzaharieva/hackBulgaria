import unittest
from Panda import Panda


class TestPandaClass(unittest.TestCase):

    def setUp(self):
        self.my_panda = Panda('Elena', 'el@pandamail.com', 'female')

    def test_initialisation(self):
        self.assertTrue(isinstance(self.my_panda, Panda))

    def test_name(self):
        self.assertEqual(self.my_panda.panda_name, self.my_panda.name1())

    def test_mail(self):
        self.assertEqual(self.my_panda.mail, self.my_panda.email())

    def test_gender(self):
        self.assertEqual(self.my_panda.sex, self.my_panda.gender())

    def test_is_male_female(self):
        self.assertTrue(self.my_panda.isFemale())
        self.assertFalse(self.my_panda.isMale())

    def test_str_cast(self):
        wanted = 'Elena'
        self.assertEqual(wanted, self.my_panda.__str__())

    def test_eq(self):
        my_other_panda = Panda('Elena', 'el@pandamail.com', 'female')
        self.assertTrue(self.my_panda.__eq__(my_other_panda))

    def test_hash(self):
        self.assertEqual(self.my_panda.__hash__(), hash(self.my_panda.mail))

    def test_repr(self):
        self.assertEqual(self.my_panda.__repr__(),  "Panda('Elena', 'el@pandamail.com', 'female')")

if __name__ == "__main__":
    unittest.main()
