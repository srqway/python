from flask import Flask, jsonify, request, Response

app = Flask(__name__)

datas = []

@app.route('/create', methods=['POST'])
def create():
    json = request.get_json()
    datas.append(json)
    return Response()

@app.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify(datas)

@app.route('/update', methods=['PUT'])
def update():
    json = request.get_json()
    datas[0] = json
    return Response()

@app.route('/delete', methods=['DELETE'])
def delete():
    del datas[0]
    return Response()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
