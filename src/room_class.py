class Room:
    def __init__(self, room_name, room_capacity, entry_fee):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.play_list = []
        self.till = 0
        self.costumer_history = {}
        self.fridge = []


    def add_song(self, song):
        self.play_list.append(song)
    
    def add_drink(self, name, price, stock):
        drink_dict = {}
        for drink in self.fridge:
            if drink["name"] == name:
                drink["price"] = price
                drink["stock"] += stock
                return
        drink_dict["name"] = name
        drink_dict["price"] = price
        drink_dict["stock"] = stock
        self.fridge.append(drink_dict)
        
    def can_check_in(self):
        if len(self.guests) < self.room_capacity:
            return True
        return False

    def is_costumer_in_database(self, costumer_name):
        if costumer_name in self.costumer_history:
            return True
        return False
    
    
    def add_costumer_to_db(self, costumer_name):
        data = {"spent_amount": 0, "visit_times": 0}
        self.costumer_history[costumer_name] = data
                    
        
    def add_to_costumer_spent(self, costumer_name, amount):
        self.costumer_history[costumer_name]["spent_amount"] += amount
        
    def make_sale(self, costumer_name, amount):
        if not self.is_costumer_in_database(costumer_name):
            self.add_costumer_to_db(costumer_name)
        self.till += amount
        self.add_to_costumer_spent(costumer_name, amount)
        return amount
            
    def sell_drink(self, costumer_name, drink_name):
        for drink in self.fridge:
            if drink["name"] == drink_name:
                if drink["stock"] == 0:
                    return False
                if self.is_vip(costumer_name):
                    drink["price"] *= 0.9
                self.make_sale(costumer_name, drink["price"])
                drink["stock"] -= 1
                return True
                
    def get_drink_price(self, drink_name):
        for drink in self.fridge:
            if drink["name"] == drink_name:
                return drink["price"]
        return False
    
    def is_vip(self, costumer_name):
        if not self.is_costumer_in_database(costumer_name):
            self.add_costumer_to_db(costumer_name)
        if self.costumer_history[costumer_name]["spent_amount"] > 100:
            return True
        return False
    
    def check_loyalty_status(self, costumer):
        if self.costumer_history[costumer.name]["visit_times"] > 100:
            return "Gold"
        elif self.costumer_history[costumer.name]["visit_times"] > 50:
            return "Silver"
        elif self.costumer_history[costumer.name]["visit_times"] > 10:
            return "Bronze"
        return "No status yet soz"
        
        
                
    
        
        

    
        