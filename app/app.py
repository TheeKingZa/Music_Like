#!/usr/bin/python3

from flask import Flask, render_template, request, url_for, redirect, flash, get_flashed_messages, jsonify
import json
# Flask app instance
app = Flask(__name__)
app.secret_key = 'admin'

# Get information of user
username = 'admin'
password = 'admin'



# Load track data from songs.json
with open('data/songs.json', 'r') as file:
    tracks = json.load(file)

def read_user_data():
    try:
        with open('user_db.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_user_data(user_data):
    users = read_user_data()
    users.append(user_data)
    with open('user_db.json', 'w') as file:
        json.dump(users, file, indent=4)
    
# Routes
@app.route('/')
def index():
    return render_template('login.html', current_page='/', tracks=tracks)

@app.route('/login', methods=['POST'])
def login():
    entered_username = request.form['username']
    entered_password = request.form['password']
    
    if entered_username == username and entered_password == password:
        return redirect(url_for('home'))
        # Redirect to home page if successful
    else:
        error = "Invalid Username or Password. Please Try Again"
        return render_template('login.html', current_page='login', error=error)

@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    username = request.form.get('username')
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    # Validate form data (e.g., check for empty fields, validate email format, etc.)
    # Add your validation code here
    
    # Check if the passwords match
    if password != confirm_password:
        # Passwords don't match, handle this case (e.g., display an error message)
        error = "Passwords do not match. Please try again."
        return render_template('sign-up.html', error=error)
    
    # Check if the user already exists (e.g., by querying the database)
    # Add your code to check if the user exists
    user_data = {
        'username': username,
        'name': name,
        'surname': surname,
        'email': email,
        'password': password
    }
    
    # If everything is valid, you can store the user in the database
    # Add your code to store the user in the database
    
    # For demonstration purposes, let's just redirect to the sign-up page again
    add_user_data(user_data)
    flash('Signup successful!', 'success')
    return redirect(url_for('home'))

@app.route('/signUp')
def signUp():
    # Render SignUp
    return render_template('sign-up.html', current_page='signUp')

@app.route('/home')
def home():
    # Render the home page
    messages = get_flashed_messages('success')
    return render_template('home.html', messages=messages)

@app.route('/search')
def search():
    search_query = request.args.get('query')
    # Simulate Database search
    search_results = [track for track in tracks if
                    search_query.lower() in track['title'].lower() or 
                    search_query.lower() in track['album'].lower() or
                    search_query.lower() in track['artist'].lower()]
    return jsonify(search_results)

@app.route('/contact')
def contact():
    # Render Contact page
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    # Render AboutUs page
    return render_template('aboutus.html')


    
if __name__ == '__main__':
    app.run(debug=True)
