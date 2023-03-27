from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/python_req_1', methods = ['GET'])
def python_req_1():
    name = request.args.get('name')
    age = request.args.get('age')
    salary = request.form.get('salary')
    car = request.form.get('car')
    
    result = {
        'user_name': name,
        'user_age': age,
        'user_salary': salary,
        'user_car': car
    }
    
    return jsonify(result)

@app.route('/python_req_2', methods = ['GET', 'POST'])
def python_req_2():
    if request.method == 'GET':
        model = request.args.get('model')
        title = request.args.get('title')
        price = int(request.form.get('price')) + 10000
        options = request.form.get('options')
        
        result = {
            'car_model': model,
            'car_title': title,
            'car_price': price,
            'car_options': options
        }

    elif request.method == 'POST':
        model = request.form.get('model')
        title = request.form.get('title')
        price = int(request.form.get('price')) + 100000
        options = request.form.get('options')
        
        result = {
            'car_model': model,
            'car_title': title,
            'car_price': price,
            'car_options': options
        }
        
    return jsonify(result), 288        

app.run(host='0.0.0.0', debug=True, port='5005')
