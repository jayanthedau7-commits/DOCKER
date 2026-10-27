from flask import Flask, jsonify
from bussiness import get_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world'


@app.route('/api', methods=['GET'])
def api():
    data = get_data()
    return jsonify({'names': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)