from flask import Flask
from data import data

app = Flask(__name__)
@app.route('/')
def name():
    return 'Welcome to Stars World'

@app.route('/stars')
def stars():
    return jsonify({
        'data': data,
        'message': 'Success'
    })

@app.route('/specificData')
def specificData():
    name = request.args.get('name')
    dataRetreive = next(i for i in data if('name') == name)
    return jsonify({
        'data':dataRetrieve,
        'message':'yayyy'
    })
