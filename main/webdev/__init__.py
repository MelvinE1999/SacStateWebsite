from flask import Flask

app = Flask(__name__)
#supposedly needed for the survey method
app.config['SECRET_KEY'] = 'Secret'

from webdev import routes
