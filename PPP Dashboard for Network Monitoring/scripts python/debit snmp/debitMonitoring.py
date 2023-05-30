from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activer la prise en charge des requêtes CORS

@app.route('/scan', methods=['POST'])
def scan():
    subnet = request.form['subnet']
    print(subnet)
    with open("taux.txt", "r") as file:
        content = file.read()

    response = {"output": content}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
