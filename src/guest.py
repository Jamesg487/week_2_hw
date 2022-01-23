class Guest:

    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    def check_favourite_song_exists(self, room):
         for song in room.songs:
             if song.track_name == self.favourite_song:
                 return "Yeeaah I love this song!" 