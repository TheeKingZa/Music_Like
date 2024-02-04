#!/usr/bin/env python3

# This file contains unit tests for the song list functionality

# Import necessary modules
import unittest

# Import the Song class from model.py
from app.model import Song

# Define a test case class
class TestSongList(unittest.TestCase):
    # Test the initialization of Song objects
    def test_song_initialization(self):
        song = Song(1, "Title", "Artist")
        self.assertEqual(song.id, 1)
        self.assertEqual(song.title, "Title")
        self.assertEqual(song.artist, "Artist")

# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()
