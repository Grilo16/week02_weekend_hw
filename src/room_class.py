class Room:
    def __init__(self, room_name, room_capacity, entry_fee):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.play_list = []
        self.till = 0

     
    def add_song(self, song):
        self.play_list.append(song)
        
    def can_check_in(self):
        if len(self.guests) >= self.room_capacity:
            return False
        return True

    
        
        

    
        