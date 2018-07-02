from flask import Flask

from flaskpython import (
    rest,
    path_param,
    redirect,
    template,
    form,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.register_blueprint(rest.bp)
app.register_blueprint(path_param.bp)
app.register_blueprint(redirect.bp)
app.register_blueprint(template.bp)
app.register_blueprint(form.bp)
