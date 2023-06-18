#backend for the website.

from flask import Flask
from queries import make_query, query_postgres
from functions import decide, initialize_email 
from flask import jsonify

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    query_postgres('INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (1, "test", "test")')
    query_postgres('ISERT INTO EmailAttributes (attribute_id, email_id, name, role, description, authority, department), VALUES (1, 1, "test", "test", "test", "test", "test")')
    return 'OK'

@app.route('/get', methods=['GET'])
def get():
    query_postgres('SELECT * FROM EmailAddresses where emailaddresses.user_id = "test"')
    return 'OK'

@app.route('/delete', methods=['DELETE'])
def delete():
    query_postgres('DELETE FROM EmailAddresses WHERE email_id = "test"')
    return 'OK'

@app.route('/create', methods=['PUT'])
def create():
    query_postgres('INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (1, "test", "test")')

@app.route('/signup', methods=['POST'])
def signup():
    if len(query_postgres('SELECT * FROM Users WHERE username = "test"')) > 0:
        return 'Username already exists'
    
    #create the new database for the user, from functions.py
    #initialize_email()

    query_postgres('INSERT INTO Users (user_id, username, password) VALUES (1, "test", "test")')
    return 'OK'

@app.route('/login', methods=['POST'])
def login():
    l = query_postgres('SELECT * FROM Users WHERE username = "test" AND password = "test"')
    if len(l) == 0:
        return 'Invalid username or password'
    return jsonify({'success': True, 'ok': True})



if __name__ == '__main__':
    app.run()
