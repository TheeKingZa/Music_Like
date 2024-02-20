#!/usr/bin/python3
import requests
import configparser
from flask import (
    Flask, render_template,
    request, url_for,
    redirect, flash,
    get_flashed_messages,
    jsonify, session
)
from db import read_user_data, add_user_data
import json

# Flask app instance
app = Flask(__name__)
app.secret_key  = 'admin'

# Load track data from songs.json
with open('data/songs.json', 'r') as file:
    tracks = json.load(file)

# Count Users
def count_users():
    with open('.user_db.json') as file:
        user_data = json.load(file)
        return len(user_data)


# Routes
@app.route('/')
def index():
    return render_template('login.html', current_page='/', tracks=tracks)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle login form submission
        entered_username = request.form['username']
        entered_password = request.form['password']
        
        # Load user data
        user_data = read_user_data()
        
        # check if the entered user and paswd is matching
        for user in user_data:
            if user['username'] == entered_username and user['password'] == entered_password:
                # Store the entered usernae in the session
                session['entered_username'] = entered_username
                return redirect(url_for('home'))
            # Redirect to home page if successful
            else:
                error = "Invalid Username or Password. Please Try Again"
                return render_template('login.html', current_page='login', error=error)
    else:
        # if it's a GET request, Render the lofin page.
        return render_template('login.html', current_page='login')


@app.route("/username")
def username():
    if "username" in session:
        username = session['username']
        return f"<h1>{ username }</h1>"
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('entered_username', None)
    # Redirect user to login page
    return redirect(url_for('login'))

# sign-up Logic
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
    # Add  validation code here
    
    # Check if the passwords match
    if password != confirm_password:
        # Passwords don't match, handle this case (e.g., display an error message)
        error = "Passwords do not match."
        return render_template('sign-up.html', error=error, show_navbar=False)
    
    # Check if the user already exists (e.g., by querying the database)
    # Add your code to check if the user exists
    user_data = read_user_data()
    for user in user_data:
        if user['username'] == username:
            # user already exist, handle
            error = "Username already exist"
            return render_template('sign-up.html', error=error, show_navbar=False) 
    
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
    session['entered_username'] = username
    return redirect(url_for('home'))


# Sign-up redirect
@app.route('/signUp')
def signUp():
    # Render SignUp
    show_navbar = request.args.get('show_navbar', True)
    return render_template('sign-up.html', current_page='signUp', show_navbar=show_navbar)

@app.route('/home')
def home():
    # Pass the username to the template
    username = session.get('entered_username', 'Guest')
    user_count = count_users()
    # Render the home page
    messages = get_flashed_messages('success')
    return render_template('home.html', messages=messages, current_page='home', username=username, user_count=user_count)

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
    user_count = count_users()
    # Pass the username to the template
    username = session.get('entered_username', 'Guest')
    return render_template('contact.html', current_page='contact', username=username, user_count=user_count)

@app.route('/aboutus')
def aboutus():
    # Render AboutUs page
    user_count = count_users()
    # Pass the username to the template
    username = session.get('entered_username', 'Guest')
    return render_template('aboutus.html', current_page='aboutus', username=username, user_count=user_count)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))