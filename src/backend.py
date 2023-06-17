#backend for the website.

from flask import Flask
from queries import make_query
from functions import decide, initialize_email

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    make_query('INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (1, "test", "test")')
    make_query('ISERT INTO EmailAttributes (attribute_id, email_id, name, role, description, authority, department), VALUES (1, 1, "test", "test", "test", "test", "test")')
    return 'OK'

@app.route('/get', methods=['GET'])
def get():
    make_query('SELECT * FROM EmailAddresses where userid = "test"')
    return 'OK'

@app.route('/delete', methods=['DELETE'])
def delete():
    make_query('DELETE FROM EmailAddresses WHERE email_id = "test"')
    return 'OK'

@app.route('/create', methods=['PUT'])
def create():
    make_query('INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (1, "test", "test")')
    make_query('')

@app.route('/signup', methods=['POST'])
def signup():
    if len(make_query('SELECT * FROM Users WHERE username = "test"')) > 0:
        return 'Username already exists'
    
    #create the new database for the user, from functions.py
    initialize_email()

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
