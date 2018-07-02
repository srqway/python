from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash

bp = Blueprint('form', __name__, url_prefix='/form')

@bp.route('/index', methods=['GET'])
def index():
    return render_template('form/form.html')

@bp.route('/post', methods=['POST'])
def post():
    criteria = request.form
    flash(criteria, "criteria")
    flash("should not shown !!!", "not_used")
    return redirect(url_for('form.index'))