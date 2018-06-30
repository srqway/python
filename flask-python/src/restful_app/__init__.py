from flask import Flask

from restful_app.crud import crud

app = Flask(__name__)
app.register_blueprint(crud)

