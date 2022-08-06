import unittest
from src.guest_class import Guest
from src.room_class import Room
from src.song_class import Song

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up mock songs
        self.rickRoll = Song("Never Gonna Give You Up", "Rick Astley")
        self.friday = Song("Friday", "Rebecca Black")
        self.gangnam = Song("Gangnam Style", "PSY")

        # Set up mock room objects to do tests on
        self.room1 = Room("Le Room of Le Test LOL", 20, 10)
        self.room2 = Room("Le Room of Silence", 5, 5)
        self.room3 = Room("Le Tiny Room", 1, 50)

        # Set up mock guests
        self.dr_yan_nitor = Guest("Dr.Yan Nitor", 1000, self.rickRoll)
        self.shanda_leer = Guest("Shanda Leer", 1000, self.gangnam)
        self.ben_dover = Guest("Ben Dover", 1000, self.friday)
        
        # Add drinks to room1
        self.room1.add_drink("Whisky", 30, 10)
        self.room1.add_drink("Wine", 20, 10)
        self.room1.add_drink("Beer", 10, 10)
        
        # Add drinks to room2
        self.room2.add_drink("Milk", 10, 10)
        self.room2.add_drink("Water", 5, 10)
        
        # Add drinks to room3
        self.room3.add_drink("Whisky Omega Special", 50, 10)
        
        # Make shanda_leer Vip on room1
        self.shanda_leer.enter_room(self.room1)
        self.shanda_leer.buy_drink("Wine")
        self.shanda_leer.buy_drink("Wine")
        self.shanda_leer.buy_drink("Wine")
        self.shanda_leer.buy_drink("Wine")
        self.shanda_leer.buy_drink("Beer")
        self.shanda_leer.leave_room()
        
  

        # Make ben_dover Vip on room2
        self.ben_dover.enter_room(self.room2)
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Milk")
        self.ben_dover.buy_drink("Water")
        self.ben_dover.leave_room()
        
    


        # Make dr_yan_nitor Vip on room3
        self.dr_yan_nitor.enter_room(self.room3)
        self.dr_yan_nitor.buy_drink("Whisky Omega Special")
        self.dr_yan_nitor.leave_room()
       
        
    def test_room_tills(self):
        self.assertEqual(100, self.room1.till)
        self.assertEqual(100, self.room2.till)
        self.assertEqual(100, self.room3.till)
        
    def test_wallets(self):
        self.assertEqual(900, self.shanda_leer.wallet)
        self.assertEqual(900, self.ben_dover.wallet)
        self.assertEqual(900, self.dr_yan_nitor.wallet)
        
    # Test next time guests enter bars they are vips
    def test_vips(self):
        self.shanda_leer.enter_room(self.room1)
        self.ben_dover.enter_room(self.room2)
        self.dr_yan_nitor.enter_room(self.room3)
        self.assertEqual(True, self.room1.is_vip(self.shanda_leer.name))
        self.assertEqual(True, self.room2.is_vip(self.ben_dover.name))
        self.assertEqual(True, self.room3.is_vip(self.dr_yan_nitor.name))

    # Test not vip in other bars
    def test_not_vip_elsewhere(self):
        self.shanda_leer.enter_room(self.room2)
        self.ben_dover.enter_room(self.room3)
        self.dr_yan_nitor.enter_room(self.room1)
        self.assertEqual(False, self.room2.is_vip(self.shanda_leer.name))
        self.assertEqual(False, self.room3.is_vip(self.ben_dover.name))
        self.assertEqual(False, self.room1.is_vip(self.dr_yan_nitor.name))
        
    # test vips get discounts
    def test_vip_gets_discount(self):
        self.shanda_leer.enter_room(self.room1)
        self.ben_dover.enter_room(self.room2)
        self.dr_yan_nitor.enter_room(self.room3)
        
        # Buy drinks at discount
        self.dr_yan_nitor.buy_drink("Whisky Omega Special")
        self.ben_dover.buy_drink("Milk")
        self.shanda_leer.buy_drink("Beer")

        # Test wallets
        self.assertEqual(881, self.shanda_leer.wallet)
        self.assertEqual(886, self.ben_dover.wallet)
        self.assertEqual(805, self.dr_yan_nitor.wallet)

        # Test tills
        self.assertEqual(119, self.room1.till)
        self.assertEqual(114, self.room2.till)
        self.assertEqual(195, self.room3.till)