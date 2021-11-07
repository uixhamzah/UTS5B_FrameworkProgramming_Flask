
from application import app
from flask import Flask, render_template, url_for



@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/auth')
def login():
    return render_template('/auth.html')

@app.route('/contact-us')
def contactUs():
    return render_template('contact-us.html')


if __name__ == '__main__':
    app.run(debug=True)