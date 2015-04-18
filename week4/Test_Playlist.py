import unittest
from music_library import Song
from music_library import Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.code_songs = Playlist(name="Code", repeat=True, shuffle=True)

    def test_initialisation(self):
        self.assertTrue(isinstance(self.code_songs, Playlist))

    def test_add_remove_song(self):
        a = Song()
        self.assertFalse(a in self.code_songs.song_list)
        self.code_songs.add_song(a)
        self.assertTrue(a in self.code_songs.song_list)
        self.code_songs.remove_song(a)
        self.assertTrue(a not in self.code_songs.song_list)

    def test_add_songs(self):
        a = Song()
        b = Song(title="Pesho's song", artist="Pesho",
                 album="Pesho/'s album", length="23:22:12")
        l = []
        l.append(a)
        l.append(b)
        self.code_songs.add_songs(l)
        self.assertTrue(a in self.code_songs.song_list)
        self.assertTrue(b in self.code_songs.song_list)

    def test_artists_histogram(self):
        a = Song(title="alaba", artist="Rihanna",
                 album="Nqkoi", length="12:02")
        b = Song(title="Pesho's song", artist="Pesho",
                 album="Pesho/'s album", length="23:22:12")
        c = Song(title="PeshosOtherSong", artist="Pesho",
                 album="blaa", length="22:12")
        self.code_songs.song_list.append(a)
        self.code_songs.song_list.append(b)
        self.code_songs.song_list.append(c)
        dicta = {}
        dicta['Pesho'] = 2
        dicta['Rihanna'] = 1
        self.assertEqual(dicta, self.code_songs.artists())

    def test_total_length(self):
        a = Song(title="alaba", artist="Rihanna",
                 album="Nqkoi", length="12:02")
        b = Song(title="Pesho's song", artist="Pesho",
                 album="Pesho/'s album", length="23:22:12")
        c = Song(title="PeshosOtherSong", artist="Pesho",
                 album="blaa", length="22:12")
        self.code_songs.song_list.append(a)
        self.code_songs.song_list.append(b)
        self.code_songs.song_list.append(c)
        self.assertEqual(self.code_songs.total_length(), '23:56:26')


if __name__ == "__main__":
    unittest.main()
