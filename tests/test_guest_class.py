import unittest
from src.guest_class import Guest
from src.song_class import Song
from src.room_class import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        # Create a mock song to add to guest
        self.song = Song("Never Gonna Give You Up", "Rick Astley")
        
        # Create a mock guest to test
        self.guest = Guest("Mike Lytoris", 69, self.song)
        
        # Create a mock Room to test on
        self.room = Room("The Situation Room", 10)
        
    # Test guest name is "Mike Lytoris" 
    def test_guest_has_name(self):
        self.assertEqual("Mike Lytoris", self.guest.name)

    # Test wallet is 69 
    def test_guest_has_wallet(self):
        self.assertEqual(69, self.guest.wallet)

    # Test favorite song is self.song
    def test_guest_has_favorite_song(self):
        self.assertEqual(self.song, self.guest.favorite_song)

    # Test current room is None
    def test_current_room_is_none(self):
        self.assertEqual(None, self.guest.current_room)
        
    # Test guest can enter room
    def test_enter_room_success(self):
        self.guest.enter_room(self.room)
        self.assertEqual(True, self.guest.name in self.room.guests)
        self.assertEqual(self.room, self.guest.current_room)

    def test_enter_room_failed_full(self):
        self.room.room_capacity = 0
        self.guest.enter_room(self.room)
        self.assertEqual(False, self.guest.name in self.room.guests)
        self.assertEqual(None, self.guest.current_room)

    # Test guest can leave room
    def test_leave_room(self):
        self.guest.enter_room(self.room)
        self.guest.leave_room()
        self.assertEqual(False, self.guest.name in self.room.guests)
        self.assertEqual(None, self.guest.current_room)

    