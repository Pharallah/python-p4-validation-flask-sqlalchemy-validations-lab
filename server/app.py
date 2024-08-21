from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

if __name__ == '__main__':
    app.run(port=5555, debug=True)




# This is a test-driven lab.

# Run pipenv install to create your virtual environment and pipenv shell to enter the virtual environment.

# pipenv install && pipenv shell
# This project has starter code for a couple of models, Author and Post. To get create the database from the initial migration, run:

#  cd server
#  flask db upgrade
#  python seed.py
# Basic Validations
# Add validators to the Author and Post models such that:

# All authors have a name.
# No two authors have the same name.
# Author phone numbers are exactly ten digits.
# Post content is at least 250 characters long.
# Post summary is a maximum of 250 characters.
# Post category is either Fiction or Non-Fiction.
# Post title is sufficiently clickbait-y and must contain one of the following:
# "Won't Believe"
# "Secret"
# "Top"
# "Guess"
# You should not need to run another migration, unless you altered model constraints.

# Run pytest -x to run your tests. Use these instructions and pytest's error messages to complete your work in the server/ folder.