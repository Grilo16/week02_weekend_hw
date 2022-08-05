class Room:
    def __init__(self, room_name, room_capacity, entry_fee):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.play_list = []
        self.till = 0
        self.costumer_spending_history = {}

     
    def add_song(self, song):
        self.play_list.append(song)
        
    def can_check_in(self):
        if len(self.guests) >= self.room_capacity:
            return False
        return True

    def is_costumer_in_database(self, costumer_name):
        if costumer_name in self.costumer_spending_history:
            return True
        return False
    
    
    def add_costumer_to_db(self, costumer_name):
        self.costumer_spending_history[costumer_name] = 0            
        
    def add_to_costumer_spent(self, costumer_name, amount):
        self.costumer_spending_history[costumer_name] += amount
        
    def make_sale(self, costumer_name, amount):
        if not self.is_costumer_in_database(costumer_name):
            self.add_costumer_to_db(costumer_name)
        self.till += amount
        self.add_to_costumer_spent(costumer_name, amount)       
    
        
        

    
        