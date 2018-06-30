from flask import Blueprint, jsonify, request, Response

rest = Blueprint('rest', __name__)

datas = []


@rest.route('/create', methods=['POST'])
def create():
    json = request.get_json()
    datas.append(json)
    return Response()


@rest.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify(datas)


@rest.route('/update', methods=['PUT'])
def update():
    json = request.get_json()
    datas[0] = json
    return Response()


@rest.route('/delete', methods=['DELETE'])
def delete():
    del datas[0]
    return Response()
