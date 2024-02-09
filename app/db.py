#!/usr/bin/env python3
'''
This file handles database operations
# Import necessary modules
'''

import json

def read_user_data():
    try:
        with open('.user_db.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_user_data(user_data):
    # Read existing user data from the database
    users = read_user_data()
    
    # Check if the username already exists
    for user in users:
        if user['username'] == user_data['username']:
            # Username already exists, handle this case
            # display error message
            print("Username already exists.")
            return
    
    # If username is unique, add the new user data to list
    users.append(user_data)
    
    # Write the updated user data back to the database file
    with open('.user_db.json', 'w') as file:
        json.dump(users, file, indent=4)
