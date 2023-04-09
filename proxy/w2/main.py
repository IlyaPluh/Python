from flask import Flask, request, jsonify
import requests
from requests.exceptions import ConnectionError


app = Flask(__name__)


gift_list = {'junior':['mac', 'coffee', 'fruits'],
             'middle':['junior+', 'gym', 'medical_ensurance_500'],
             'senior':['middle+', 'medical_ensurance_500', 'taxi', 'parking']}




@app.route('/get_pack', methods=['POST'])
def r_employee_pack():



    employee_level = request.json['employee_level']


    if employee_level in gift_list:

        pack_title = employee_level + '_pack'

        employee_gift_pack = {pack_title: gift_list[employee_level]}

        return jsonify(employee_gift_pack)











