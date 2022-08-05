class Guest:
    def __init__(self, name, wallet, favorite_song):
        self.name = name
        self.wallet = wallet
        self.favorite_song = favorite_song
        self.current_room = None
        
        
    def enter_room(self, room):
        if room.can_check_in():
            room.guests.append(self.name)
            self.current_room = room
        
    def leave_room(self):
        self.current_room.guests.remove(self.name)
        self.current_room = None