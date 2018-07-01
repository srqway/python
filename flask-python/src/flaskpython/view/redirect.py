from flask import Blueprint, redirect, url_for

bp = Blueprint('redirect', __name__, url_prefix='/redirect')


@bp.route('/login/<param>', methods=['GET'])
def login(param):
    if param == 'admin':
        return redirect(url_for('redirect.admin'))
    else:
        return redirect(url_for('redirect.guess', name=param))


@bp.route('/admin', methods=['GET'])
def admin():
    return "hello."


@bp.route('/guess/<name>', methods=['GET'])
def guess(name):
    return "hello %s" % name

