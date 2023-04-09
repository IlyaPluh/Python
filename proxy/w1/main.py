from flask import Flask, request, jsonify
import requests, json
from requests.exceptions import ConnectionError


app = Flask(__name__)


@app.route('/employee_pack', methods=['GET'])
def r_employee_pack():

    url = 'http://0.0.0.0:5301/get_pack'

    employee_level = request.args.get('employee_level')

    employee_levels = ['junior', 'middle', 'senior']

    if employee_level in employee_levels:
        employee_level_req = {'employee_level': employee_level}

        error_resp_mess = employee_level + ' --==-- Proxy online but ws1 is offline'

        try:
            req = requests.post(url, json=employee_level_req).json()

            return jsonify(req)
        except requests.exceptions.ConnectionError as e:
            return error_resp_mess
    else:
        return 'Undefined level'













