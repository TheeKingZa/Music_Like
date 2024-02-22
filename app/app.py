#!/usr/bin/python3
from flask import (
    Flask, render_template,
    request, url_for,
    redirect, flash,
    get_flashed_messages,
    jsonify, session
)
from db import (
    read_user_data, add_user_data
)
import json

# Flask app instance
app = Flask(__name__)
app.secret_key = 'admin'

# Load track data from songs.json
with open('data/songs.json', 'r') as file:
    tracks = json.load(file)


def count_users():
    """Count the number of users in the database."""
    with open('.user_db.json') as file:
        user_data = json.load(file)
        return len(user_data)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('login.html', current_page='/', tracks=tracks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']
        user_data = read_user_data()
        for user in user_data:
            if user['username'] == entered_username and user['password'] == entered_password:
                session['entered_username'] = entered_username
                return redirect(url_for('home'))
        else:
            error = "Invalid Username or Password. Please Try Again"
            return render_template(
                'login.html',
                current_page='login',
                error=error
            )
    else:
        return render_template('login.html', current_page='login')


@app.route("/username")
def username():
    """Return the username."""
    if "username" in session:
        username = session['username']
        return f"<h1>{username}</h1>"
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('entered_username', None)
    return redirect(url_for('login'))


@app.route('/signup', methods=['POST'])
def signup():
    """Handle user signup."""
    username = request.form.get('username')
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        error = "Passwords do not match."
        return render_template('sign-up.html', error=error, show_navbar=False)

    user_data = read_user_data()
    for user in user_data:
        if user['username'] == username:
            error = "Username already exists"
            return render_template(
                'sign-up.html',
                error=error,
                show_navbar=False
            )

    user_data = {
        'username': username,
        'name': name,
        'surname': surname,
        'email': email,
        'password': password
    }

    add_user_data(user_data)
    flash('Signup successful!', 'success')
    session['entered_username'] = username
    return redirect(url_for('home'))


@app.route('/signUp')
def signUp():
    """Render the sign-up page."""
    show_navbar = request.args.get('show_navbar', True)
    return render_template(
        'sign-up.html', current_page='signUp',
        show_navbar=show_navbar
    )


@app.route('/home')
def home():
    """Render the home page."""
    username = session.get('entered_username', 'Guest')
    user_count = count_users()
    messages = get_flashed_messages('success')
    return render_template(
        'home.html', messages=messages,
        current_page='home', username=username,
        user_count=user_count
    )


@app.route('/search')
def search():
    """Search for tracks."""
    search_query = request.args.get('query')
    search_results = [track for track in tracks if
                      search_query.lower() in track['title'].lower() or
                      search_query.lower() in track['album'].lower() or
                      search_query.lower() in track['artist'].lower()
                      ]
    return jsonify(search_results)


@app.route('/contact')
def contact():
    """Render the contact page."""
    user_count = count_users()
    username = session.get('entered_username', 'Guest')
    return render_template(
        'contact.html', current_page='contact',
        username=username, user_count=user_count
    )


@app.route('/aboutus')
def aboutus():
    """Render the about us page."""
    user_count = count_users()
    username = session.get('entered_username', 'Guest')
    return render_template(
        'aboutus.html', current_page='aboutus',
        username=username, user_count=user_count
    )

@app.route('/profile')
def profile():
    """Render the profile page."""
    # Retrieve the current user's information from the session
    username = session.get('entered_username')
    user_data = read_user_data()
    current_user = None
    for user in user_data:
        if user['username'] == username:
            current_user = user
            break

    if current_user:
        return render_template('profile.html', current_page='profile', user=current_user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
