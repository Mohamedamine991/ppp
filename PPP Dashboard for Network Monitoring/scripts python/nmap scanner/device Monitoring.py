from flask import Flask, request, jsonify
from flask_cors import CORS
from scanner import scan_network,parse_snmp_scan_results

app = Flask(__name__)
CORS(app)  # Activer la prise en charge des requêtes CORS

@app.route('/scan', methods=['POST'])
def scan():
    subnet = request.form['subnet']
    # Faire quelque chose avec le subnet ici...
    r=scan_network(subnet)
    output = r
    response = {'output': output}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
