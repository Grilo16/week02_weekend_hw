import unittest
from src.room_class import Room
from src.guest_class import Guest
from src.song_class import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        # Set up mock songs
        self.rickRoll = Song("Never Gonna Give You Up", "Rick Astley")
        self.friday = Song("Friday", "Rebecca Black")
        self.gangnam = Song("Gangnam Style", "PSY")

        # Set up mock room objects to do tests on
        self.room1 = Room("Le Room of Le Test LOL", 20, 5)
        self.room2 = Room("Le Room of Silence", 5, 2)
        self.room3 = Room("Le Tiny Room", 1, 100)

    # Test room has a name
    def test_room_name(self):
        self.assertEqual("Le Room of Le Test LOL", self.room1.room_name)
        self.assertEqual("Le Room of Silence", self.room2.room_name)
        self.assertEqual("Le Tiny Room", self.room3.room_name)
        
    # Test room has capacity
    def test_room_has_capacity(self):
        self.assertEqual(20, self.room1.room_capacity)
        self.assertEqual(5, self.room2.room_capacity)
        self.assertEqual(1, self.room3.room_capacity)
        
    # Test room has entry fee
    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room1.entry_fee)
        self.assertEqual(2, self.room2.entry_fee)
        self.assertEqual(100, self.room3.entry_fee)

    # Test rooms have no guests to start with
        self.assertEqual(0, len(self.room1.guests))
        self.assertEqual(0, len(self.room2.guests))
        self.assertEqual(0, len(self.room3.guests))

    # Test rooms have empty playlists
    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room1.play_list))
        self.assertEqual(0, len(self.room2.play_list))
        self.assertEqual(0, len(self.room3.play_list))
        
    # Test rooms have a till
    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)
        self.assertEqual(0, self.room2.till)
        self.assertEqual(0, self.room3.till)
        
    # Test adding songs to playlist
    def test_add_songs_to_playlists(self):
        # Add all songs to room 1
        self.room1.add_song(self.rickRoll)
        self.room1.add_song(self.friday)
        self.room1.add_song(self.gangnam)
        # Add 1 song to room 3
        self.room3.add_song(self.gangnam)

        self.assertEqual(3, len(self.room1.play_list))
        self.assertEqual(0, len(self.room2.play_list))
        self.assertEqual(1, len(self.room3.play_list))
     
    # test can check guests in 
    def test_can_check_in(self):
        self.room1.guests = range(20)
        self.room2.guests = range(4)
        self.assertEqual(False, self.room1.can_check_in())
        self.assertEqual(True, self.room2.can_check_in())
        self.assertEqual(True, self.room3.can_check_in())
    
    
    
    
    
    