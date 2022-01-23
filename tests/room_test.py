import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 4, 10.00, 100.00)
        self.guest_1 = Guest("Dave", 40.00, "Alberto Balsalm")
        self.guest_2 = Guest("Bob", 10.00, "Living on a Prayer")
        self.guest_3 = Guest("Clive", 15.00, "Man I feel Like a Woman")
        self.guest_4 = Guest("Cerrie", 20.00, "Raining Blood"), 
        self.guest_5 = Guest("Greg", 3.00, "Hips Don't Lie")
        self.song_1 = Song("Alberto Balsalm", "Aphex Twin")

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_size(self):
        self.assertEqual(4, self.room_1.room_size)

    def test_number_of_guests_in_room(self):
        self.assertEqual(0, self.room_1.get_number_of_guests(self.room_1.guests))

    def test_check_in_guest_to_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.get_number_of_guests(self.room_1.guests))

    def test_remove_guest_to_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_1.get_number_of_guests(self.room_1.guests))

    def test_number_of_songs_in_room(self):
        self.assertEqual(0, self.room_1.get_number_of_songs(self.room_1.songs))

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, self.room_1.get_number_of_songs(self.room_1.songs))

    def test_not_enough_space_in_room(self):
        self.room_1.guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]
        self.assertEqual("Not enough space in room 1", self.room_1.check_in_guest(self.guest_5))

    def test_room_has_fee(self):
        self.assertEqual(10.00, self.room_1.room_fee)

    def test_guest_has_enough_money(self):
        self.room_1.check_guest_has_enough_cash(self.guest_1)
        self.assertEqual(30.00, self.guest_1.cash)

    def test_guest_has_does_not_have_enough_money(self):
        self.room_1.check_guest_has_enough_cash(self.guest_5)
        self.assertEqual(3.00, self.guest_5.cash)

    def test_till_increase(self):
        self.room_1.check_guest_has_enough_cash(self.guest_1)
        self.assertEqual(110.00, self.room_1.till)