import unittest
from music_library import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.s = Song(title="Odin", artist="Manowar",
                      album="The Sons of Odin", length="3:44")

    def test_initialisation(self):
        self.assertTrue(isinstance(self.s, Song))

    def test_str_cast(self):
        expected = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(expected, self.s.__str__())

    def test_equal(self):
        r = Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length="3:44")
        p = Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length="3:40")
        self.assertTrue(self.s.__eq__(r))
        self.assertFalse(self.s.__eq__(p))

    def test_hash(self):
        self.assertTrue(isinstance(self.s.__hash__(), int))

    def test_lenght_func(self):
        r = Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length="12:03:44")
        self.assertEqual(r.length_func(minutes=True), '03')
        self.assertEqual(r.length_func(seconds=True), '44')
        self.assertEqual(r.length_func(hours=True), '12')
        self.assertEqual(r.length_func(), r.length)

if __name__ == "__main__":
    unittest.main()
