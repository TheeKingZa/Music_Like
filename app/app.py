#!/usr/bin/python3

from flask import Flask, render_template, request, url_for, redirect

# Flask app instance
app = Flask(__name__)

username = 'admin'
password = 'admin'

# Routes
@app.route('/')
def index():
    return render_template('login.html', current_page='/')

@app.route('/login', methods=['POST'])
def login():
    entered_username = request.form['username']
    entered_password = request.form['password']
    
    if entered_username == username and entered_password == password:
        return redirect(url_for('home'))  # Redirect to home page if successful
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
    
    # If everything is valid, you can store the user in the database
    # Add your code to store the user in the database
    
    # For demonstration purposes, let's just redirect to the sign-up page again
    return redirect(url_for('signUp'))

@app.route('/home')
def home():
    return render_template('home.html')  # Render the home page

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
    
if __name__ == '__main__':
    app.run(debug=True)
