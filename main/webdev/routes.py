from flask import render_template, url_for, flash, redirect, request
from flaskblog import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/walking", methods=['GET', 'POST'])
def walking():
    return render_template('walking.html', title='Walking')

@app.route("/bus", methods=['GET', 'POST'])
def bus():
    return render_template('bus.html', title='Bus')

@app.route("/lightrail", methods=['GET', 'POST'])
def lightrail():
    return render_template('lightrail.html', title='Lightrail')

@app.route("/biking", methods=['GET', 'POST'])
def biking():
    return render_template('biking.html', title='Biking')

@app.route("/driving", methods=['GET', 'POST'])
def driving():
    return render_template('driving.html', title='Driving')