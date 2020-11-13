from flask import render_template, url_for, flash, redirect, request
from flaskblog import app
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField, SelectField


#This program and class will just provide the question variety and the question
#that the user will have to enter
class Survey(FlaskForm):
    q1 = PasswordField('What is your address?')
    choice = [(1,'Freshman'), (2,'Sophmore'), (3,'Junior'), (4,'Senior')]
    q2 = SelectField('What Year are you at Sac State:', coerce=int, choices=choice)
    q3 = TextField('What type of commute option do you use to get to school:\n')
    q4 = BooleanField('If you live on campus check the box \n')
    q5 = BooleanField('Check this box if you know about the commuter sleeve\n')
    submit = SubmitField("submit")

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

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = Survey()
    if form.is_submitted():
        result = request.form
        file = open("data.txt", "w+")
        #this will print the dat to a file
        #the file only keeps the most recent user's data for now
        #y means yes and n means no on the file
        #1-4 on the file corelates to the year they are fresman-Senior
        for key,value in result.items():
            file.write("answer to  " + str(key) + "= " + str(value) + "\n" )
        file.close()
    return  render_template('survey.html', form=form)
