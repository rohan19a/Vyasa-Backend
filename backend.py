import Flask from flask

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    # Do something here
    return 'OK'

@app.route('/get', methods=['GET'])
def get():
    # Do something here
    return 'OK'

@app.route('/delete', methods=['DELETE'])
def delete():
    # Do something here
    return 'OK'

@app.route('/create', methods=['PUT'])
def create():
    # Do something here
    return 'OK'


if __name__ == '__main__':
    app.run()
