from flask import Blueprint, render_template

bp = Blueprint('/template', __name__, url_prefix='/template')

@bp.route('/basic', methods=['GET'])
def basic():
    model = {
        "str_": "STRING",
        "int_": 3
    }
    return render_template('template/basic.html', model = model)
