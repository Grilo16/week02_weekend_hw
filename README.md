# week02_weekend_hw
Room class - 
    Initialized given a room_name(string), room_capacity(integer), and entry_fee(integer)
    the room also starts with the following parameters
    empty guest list
    empty play list
    empty till (int 0)
    a costumer history dictionary which will be used to hold the following data structure
        {guest name: {spent_amount : x, visit_times: y}}
        where x and y will be ints
    and an empty fridge list which will hold dictionaries with the following structure:
        {drink_name: "name", "price": y, "stock": x}
        where x and y are integers
    
    Room methods:
        add_song(song_object)
        appends a song object to the play_list list

        add_drink(name, price, stock)
        appends a drink dictionary to the fridge list, if the drink already exists changes only the price and adds stock to current ammount
        else appends the dictionary to the list

        can_check_in()
        this method compares the number of people in the room to the room capacity and returns true if there is space to enter the room, false if there isnt

        is_costumer_in_database(costumer_name)
        this checks if the costumer exists in the costumer_history dictionary and returns true if it is , false otherwise

        add_costumer_to_db(costumer_name)
        this adds a costumer to the database correctly formated as a dictionary with visit times and spent amount set to 0

        add_to_costumer_spent(costumer_name, amount)
        simply adds the amount to the amount the costumer has spent in the bar

        make_sale(costumer_name, amount)
        this checks if costumer is already in the database , if not it adds the costumer followed by adjusting the amount in the till and the amount in the costumer spent database

        sell_drink(costumer_name, drink_name)
        this checks if drink exists on drinks list
        if so check if the drink is available in stock 
        if so it will check if the costumer is a vip to adjust price is nescessary 
        then call the make sale function using the drinks amount
        it then reduces the drink stock amount  
        and returns True so the guest can use the output to signal a transaction

        get_drink_price(drink_name)
        gets the price of a drink in the dictionary given the name as a string

        is_vip(costumer_name)
        checks if the costumer is in the database if not add it
        next check if the costumer has spent more than 100 in the room and if so returns true for costumer is a vip
        else return false

        check_loyalty_status(costumer)
        this checks if the costumer is a gold silver or bronze costumer based on how many times they have entered the room 
        10+ = bronze
        50+ = silver
        100+ = gold



Guest class - 
    Initialized given a name(string), wallet(integer) and favorite song(Song object)
    The guest will also have a current_room which changes depending on what room they're currently in and is initialized as None
    

    Guest methods:
        The can_afford method, takes a price as an argument and checks if the guest has enough money in its wallet to afford the price

        The enter_room method, first checks if the guest can afford the room's entry fee 
        and if so checks if the guest is a vip on that room
        If guest is a vip the entry fee will be 10% cheaper
        otherwise entry fee is unchenged
        next it will check that the room as space for the guest to enter
        followed by appending the guest name to the room 
        next using the room make sale method with the guest name and the pay as parameters.
        next we increase the number of visits by 1
        and subtract the entry fee from the wallet
        and change guests current room to the current room
        lastly, if the guests favorite song is in the room the function will return "OH MY GOD THATS MY SONG HOLD MY BEER!"

        the leave room method removes the guest from the room list, and also reverts the current room back to None

    
        the buy_drink method: 
        allows the user to buy a drink by first checking the drink price and if the user is vip to adjust the price if required
        next it will check if the guest can afford the drink
        and if so call the room sell drink method and change reduce the guests wallet by the drinks price

Song class - 
    Initialized given a song name (string) and an artist(string)