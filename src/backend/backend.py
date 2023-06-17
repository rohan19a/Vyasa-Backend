#backend for the website.

from flask import Flask
import mindsdb_sdk
from queries import make_query

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
    make_query('')

@app.route('/signup', methods=['POST'])
def signup():
    make_query('INSERT INTO Users (user_id, username, password) VALUES (1, "test", "test")')
    return 'OK'

@app.route('/login', methods=['POST'])
def login():
    l = make_query('SELECT * FROM Users WHERE username = "test" AND password = "test"')
    if len(l) == 0:
        return 'Invalid username or password'
    return 'OK'



if __name__ == '__main__':
    app.run()
