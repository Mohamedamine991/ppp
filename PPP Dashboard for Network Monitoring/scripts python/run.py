    # app.py
'''from flask import Flask, request

app = Flask(__name__)

@app.route('/post_input', methods=['POST'])
def post_input():
    input_value = request.form.get('input_value')
    # Vous pouvez maintenant utiliser input_value dans votre script Python
    print(input_value)
    return 'Success', 200

if __name__ == '__main__':
    app.run(port=5005)'''
# app.py
from flask import Flask, request, jsonify
from pysnmp.hlapi import *
import time
from datetime import datetime
from functions import getter,write_result_to_file

data = (
    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.5.1')),  # RAM USED
    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.6.1'))   # RAM FREE
)

app = Flask(__name__)

@app.route('/post_input', methods=['POST'])
def get_snmp():
    targetIp = request.form.get('input_value')
    labels = ['RAM USED', 'RAM FREE']

    resultMatrix = getter(targetIp, data, labels)
    print('\n')
    print('**********************')
    print(resultMatrix[0],'\n',resultMatrix[1])
    write_result_to_file(resultMatrix)
    
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(port=5005)

