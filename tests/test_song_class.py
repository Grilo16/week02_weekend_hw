import unittest
from src.song_class import Song

class TestSong(unittest.TestCase):
    def setUp(self):
    # Set up a mock song and test it has a name and an artist
        self.song = Song("Never Gonna Give You Up", "Rick Astley")

    # Test name is "Never Gonna Give You Up" 
    def test_song_has_name(self):
        self.assertEqual("Never Gonna Give You Up", self.song.name)

    # test artist is "Rick Astley"
    def test_song_has_artist(self):
        self.assertEqual("Rick Astley", self.song.artist)