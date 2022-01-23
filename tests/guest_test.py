import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Dave", 40.00, "Alberto Balsalm")
        self.room_1 = Room(1, 5, 8.00, 50.00)
        self.song_1 = Song("Alberto Balsalm", "Aphex Twin")

    def test_guest_has_name(self):
        self.assertEqual("Dave", self.guest_1.name)

    def test_guest_has_cash(self):
        self.assertEqual(40.00, self.guest_1.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Alberto Balsalm", self.guest_1.favourite_song)

    def test_check_guest_favourite_song_is_in_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual("Yeeaah I love this song!", self.guest_1.check_favourite_song_exists(self.room_1))