# MusiqApp/app/model.py

"""Machine learning model logic."""

# Add your machine learning model code here with comments explaining its functionality.

#!/usr/bin/env python3
'''
This file defines data models
Define the Song class
'''
class Song:
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist
