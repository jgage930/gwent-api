from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/person/')
def hello():
    return jsonify({'name': 'jack', 'address': 'wisco'})

if __name__ == '__main__':
    app.run()