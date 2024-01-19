#!/usr/bin/python3
import unittest
from app.model import load_songs_data
import os

class TestSongList(unittest.TestCase):

    def test_load_songs_data(self):
        '''
        Test if songs data is loaded successfully
        '''
        # Print the current working directory
        print("Current working directory:", os.getcwd())

        # Update the file path to an absolute path
        abs_file_path = os.path.abspath('Music_like/data/songs.json')

        # Test if songs data is loaded successfully
        songs_data = load_songs_data(abs_file_path)
        self.assertTrue(songs_data, "Failed to load songs data")

'''
If this script is run directly (not imported), run the tests
'''
if __name__ == '__main__':
    unittest.main()
