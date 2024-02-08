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
    users = read_user_data()
    users.append(user_data)
    with open('.user_db.json', 'w') as file:
        json.dump(users, file, indent=4)
