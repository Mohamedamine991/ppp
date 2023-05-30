from flask import Flask, request

app = Flask(__name__)

@app.route('/post_input', methods=['POST'])
def post_input():
    input_value = request.form['input_value']
    # Faites quelque chose avec la valeur de l'input
    print("Valeur de l'input :", input_value)
    return 'OK'

if __name__ == '__main__':
    app.run(host='localhost', port=5005)
