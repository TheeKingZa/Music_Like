#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

# Add more routes and functionality as needed

if __name__ == '__main__':
    app.run(debug=True)

