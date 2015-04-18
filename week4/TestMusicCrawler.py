import unittest
from music_library import MusicCrawler
from music_library import Song
from music_library import Playlist


class TestMusicCrawler(unittest.TestCase):

    def setUp(self):
        self.my_crawl = MusicCrawler("/home/elena/hackBG/My_songs")

    def test_initialisation(self):
        self.assertIsInstance(self.my_crawl, MusicCrawler)

    def test_generate_playlist(self):
        a = self.my_crawl.generate_playlist()
        for sng in range(0, len(a.song_list)):
            self.assertIsInstance(a.song_list[sng], Song)
        self.assertIsInstance(a, Playlist)

if __name__ == "__main__":
    unittest.main()
