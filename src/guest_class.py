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
            pay = room.entry_fee
            if room.is_vip(self.name):
                pay *= 0.9
            if room.can_check_in():
                room.guests.append(self.name)
                room.make_sale(self.name, pay)
                room.costumer_history[self.name]["visit_times"] += 1
                self.wallet -= pay
                self.current_room = room
                if self.favorite_song in room.play_list:
                    return "OH MY GOD THATS MY SONG HOLD MY BEER!"
        
    def leave_room(self):
        self.current_room.guests.remove(self.name)
        self.current_room = None
        
        
    def buy_drink(self, drink_name):
        if drink_price := self.current_room.get_drink_price(drink_name):
            if self.current_room.is_vip(self.name):
                drink_price *= 0.9
            if self.can_afford(drink_price):
                if self.current_room.sell_drink(self.name, drink_name):
                    self.wallet -= drink_price
            
