from flask import Flask

from flaskpython.view import (
    rest, 
    path_param,
)

app = Flask(__name__)
app.register_blueprint(rest.bp)
app.register_blueprint(path_param.bp)
