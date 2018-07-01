from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash, get_flashed_messages

bp = Blueprint('form', __name__, url_prefix='/form')

@bp.route('/index', methods=['GET'])
def index():
    
    print(get_flashed_messages())
    
    return render_template('form/form.html')

@bp.route('/post', methods=['POST'])
def post():
    criteria = request.form
    flash(criteria)
    return redirect(url_for('form.index'))