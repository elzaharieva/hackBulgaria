import unittest
from Panda import Panda
from Panda import PandaSocialNetwork


class TestSocialPandaNetwork(unittest.TestCase):

    def setUp(self):
        self.eli = Panda('Elena', 'el@pandamail.com', 'female')
        self.koko = Panda('Koko', 'koko@pandamail.com', 'male')
        self.network = PandaSocialNetwork()
        self.network.panda_list[self.eli] = []
        self.network.panda_list[self.koko] = []

    def test_initialisation(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_adding_a_panda(self):
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.assertEqual(self.network.add_panda(rado), self.network.panda_list)

    def test_exception_in_add_panda(self):
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.network.add_panda(rado)
        with self.assertRaises(ValueError):
            self.network.add_panda(rado)

    def test_has_panda(self):
        self.assertTrue(self.network.has_panda(self.eli))
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.assertFalse(self.network.has_panda(rado))

    def test_are_friends(self):
        self.assertFalse(self.network.are_friends(self.eli, self.koko))
        (self.network.panda_list[self.eli]).append(self.koko)
        (self.network.panda_list[self.koko]).append(self.eli)
        self.assertTrue(self.network.are_friends(self.eli, self.koko))

    def test_friends_of(self):
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.assertFalse(self.network.friends_of(rado))
        (self.network.panda_list[self.koko]).append(self.eli)
        self.assertEqual(
            self.network.panda_list[self.koko], self.network.friends_of(self.koko))

    def test_make_friends(self):
        self.assertFalse(self.network.are_friends(self.eli, self.koko))
        self.network.make_friends(self.eli, self.koko)
        self.assertTrue(self.network.are_friends(self.eli, self.koko))

    def test_connection_level(self):
        self.assertEqual(
            self.network.connection_level(self.eli, self.koko), -1)
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.assertFalse(self.network.connection_level(rado, self.eli))
        self.network.make_friends(self.eli, self.koko)
        self.network.make_friends(self.eli, rado)
        self.assertEqual(self.network.connection_level(self.koko, rado), 2)

    def test_are_connected(self):
        self.assertFalse(self.network.are_connected(self.eli, self.koko))
        rado = Panda('Rado', 'rado@pandamail.com', 'male')
        self.assertFalse(self.network.are_connected(rado, self.koko))
        self.network.make_friends(self.eli, self.koko)
        self.network.make_friends(self.eli, rado)
        self.assertTrue(self.network.are_connected(self.koko, rado))



if __name__ == "__main__":
    unittest.main()
