from flask import Blueprint, jsonify

bp = Blueprint('path_param', __name__, url_prefix='/path_param')


@bp.route('/str_/<param>', methods=['GET'])
def str_(param):
    return jsonify(param);


@bp.route('/int_/<int:param>', methods=['GET'])
def int_(param):
    return jsonify(param);


@bp.route('/float_/<float:param>', methods=['GET'])
def float_(param):
    return jsonify(param);


@bp.route('/path/<path:param>', methods=['GET'])
def path(param):
    return jsonify(param);
