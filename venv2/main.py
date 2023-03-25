from flask import flask, request, jsonify

app = flask(__name__)

@app.route('/python_req_1', methods = ['GET'])
def python_req_1():
    name = request.args.get('name')
    age = request.args.get('age')
    
    result = {
        'user_name': name,
        'user_age': age
    }
    
    return jsonify(result)