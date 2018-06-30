from flask import Flask

from flaskpython.view.rest import rest

app = Flask(__name__)
app.register_blueprint(rest)

