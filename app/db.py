#!/usr/bin/env python3
'''
This file handles database operations
# Import necessary modules
'''
'''
import sqlite3


# Function to fetch song recommendations from the database
def get_recommendations():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute SQL query to fetch recommendations
    cursor.execute("SELECT * FROM recommendations")

    # Fetch data
    recommendations = cursor.fetchall()

    # Close connection
    conn.close()

    return recommendations

# Function to add user preferences to the database
def add_preference(user_id, song_id):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute SQL query to insert user preference
    cursor.execute("INSERT INTO preferences (user_id, song_id) VALUES (?, ?)", (user_id, song_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()
'''