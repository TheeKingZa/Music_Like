#!/usr/bin/python3

from flask import Flask, render_template
# from app import db

# flask(app) instance.
app = Flask(__name__)

# Define routes
@app.route('/')
# home.page
def index():
    return render_template('index.html')

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

