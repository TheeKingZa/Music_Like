#!/usr/bin/python3

from flask import Flask, render_template, request, url_for, redirect

# flask(app) instance.
app = Flask(__name__)

username = 'admin'
password = 'admin'

# Define routes
@app.route('/')
# home.page
def index():
    return render_template('login.html')

# Logins Conditions
@app.route('/login', methods=['POST'])
def login():
    # Get username and password
    entered_username = request.form['username']
    entered_password = request.form['password']
    
    # Check if the entered username and password to match values
    # Hardcopy of Admin
    if entered_username == username and entered_password == password:
        # Redirect to home page if successful
        return redirect(url_for('home'))
    else:
        error = "Invalid Username or Password. Please Try Again"
        return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
    
'''
@app.route('/recommendations')
def recommendations():
    recommendations = db.get_recommendations()
    return render_template('recommendations.html', recommendations=recommendations)

# Add more routes and functionality as needed
'''

if __name__ == '__main__':
    app.run(debug=True)
