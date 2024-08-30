"""
44.How would you create a RESTful API endpoint in Flask that returns JSON data?
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Nadim Hussain",
        "age": 30,
        "city": "Anantnag"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
