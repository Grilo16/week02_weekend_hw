class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.guests = []
        self.play_list = []
        # Rooms needs songs
     
    def add_songs(self, song):
        self.play_list.append(song)
        
    def can_check_in(self):
        if len(self.guests) >= self.room_capacity:
            return False
        return True

        
    
        
        

    
        