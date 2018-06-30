from flask import Blueprint, jsonify, request, Response

crud = Blueprint('crud', __name__)

datas = []


@crud.route('/create', methods=['POST'])
def create():
    json = request.get_json()
    datas.append(json)
    return Response()


@crud.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify(datas)


@crud.route('/update', methods=['PUT'])
def update():
    json = request.get_json()
    datas[0] = json
    return Response()


@crud.route('/delete', methods=['DELETE'])
def delete():
    del datas[0]
    return Response()
