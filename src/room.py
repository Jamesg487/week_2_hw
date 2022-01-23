class Room:

    def __init__(self, room_number, room_size, room_fee, till):
        self.room_number = room_number
        self.room_size = room_size
        self.till = till
        self.room_fee = room_fee
        self.guests = []
        self.songs = []

    def get_number_of_guests(self, guest_list):
        return len(guest_list)

    def get_number_of_songs(self, song_list):
        return len(song_list)

    def check_in_guest(self, guest):
        if self.get_number_of_guests(self.guests) == self.room_size:
            return f"Not enough space in room {self.room_number}"
        if self.check_guest_has_enough_cash(guest) == "Sorry chief, not enough cash":
            return False
        else:
            self.guests.append(guest)
            

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def check_guest_has_enough_cash(self, guest):
        if guest.cash >= self.room_fee:
            guest.cash -= self.room_fee
            self.till += self.room_fee
        else:
            return "Sorry chief, not enough cash"