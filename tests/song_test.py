import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Alberto Balsalm", "Aphex Twin")

    def test_song_has_track_name(self):
        self.assertEqual("Alberto Balsalm", self.song.track_name)

    def test_song_has_artist(self):
        self.assertEqual("Aphex Twin", self.song.artist)