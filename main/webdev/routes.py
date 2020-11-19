from flask import render_template, url_for, flash, redirect, request, Flask
from webdev import app
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField, SelectField


#This class will just provide the questions that the webpage will post to the user to answer
#Used in the survey route
class Survey(FlaskForm):
    q1 = PasswordField('What is your address?')
    choice = [(1,'Freshman'), (2,'Sophmore'), (3,'Junior'), (4,'Senior')]
    q2 = SelectField('What Year are you at Sac State:', coerce=int, choices=choice)
    q3 = TextField('What type of commute option do you use to get to school:\n')
    q4 = BooleanField('If you live on campus check the box \n')
    q5 = BooleanField('Check this box if you know about the commuter sleeve\n')
    submit = SubmitField("submit")


#These two line intialize our website using the Flask library
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'

#This will make the / route point to the same route as the /home
#/home is the homepage for the website
#input: is the web address
#output: shows the user the page with provided info from the home.html
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


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

#This route points to the survey that an user will need to fill out
#input: on this page the user will have to fill out the 5Q survey
#output: The data from question 1 will be used to calculate routes
#        The rest will just be sent to a database as set by client
@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        req = request.form

        missing = list()

        #doesnt provide feedback if missing checkbox
        for k, v in req.items():
            if v == "" or v == "Choose...":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("/survey.html", feedback=feedback)

        answer1 = request.form.get("answer1")
        answer2 = request.form.get("Q1Box1")
        answer3 = request.form.get("Select1")


        file = open("data.txt", "w+")
        file.write("\nanswer1 " + answer1 + "\nanswer2: " + answer2 + "\nanswer3: " + answer3 + "\n")

        file.close()

        return redirect(request.url)

    return render_template("/survey.html")


#needed to setup the website
#must be at the end so if you add any routes add it above here
if __name__ == '__main__':
    app.run(debug=True)
