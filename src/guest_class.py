class Guest:
    def __init__(self, name, wallet, favorite_song):
        self.name = name
        self.wallet = wallet
        self.favorite_song = favorite_song
        self.current_room = None
        
    def can_afford(self, price):
        if self.wallet >= price:
            return True
        return False
        
    def enter_room(self, room):
        if self.can_afford(room.entry_fee):
            if room.can_check_in():
                room.guests.append(self.name)
                room.till += room.entry_fee
                self.current_room = room
                self.wallet -= room.entry_fee
                if self.favorite_song in room.play_list:
                    return "OH MY GOD THATS MY SONG HOLD MY BEER!"
        
    def leave_room(self):
        self.current_room.guests.remove(self.name)
        self.current_room = None