from flask import Flask, request

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    subnet = request.form['subnet']
    # Ici, vous feriez quelque chose avec le subnet, comme scanner le réseau.
    output = 'Résultat de la numérisation pour le subnet ' + subnet
    return output

if __name__ == '__main__':
    app.run(port=5000)