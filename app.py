from crypt import methods
from dataclasses import field
from flask import Flask, jsonify
import csv

from itsdangerous import json

app = Flask(__name__)

def readCards():
    filename = 'cards.csv'

    fields = []
    rows = []

    with open(filename, 'r') as f:
        csvreader = csv.reader(f)

        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)
    return fields, rows

@app.route('/cards/<string:card_name>', methods=['GET'])
def getCardByName(card_name):
    card_name = card_name.lower()

    fields, rows = readCards()

    for row in rows:
        if card_name in row[0]:
            data = {'result': dict(zip(fields, row))}
            return jsonify(data)
    return jsonify({'result': 'card does not exist'})


if __name__ == '__main__':
    app.run(debug=True)