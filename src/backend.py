#backend for the website.

from flask import Flask
from queries import query_postgres
from flask import jsonify
from flask import request

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
    login = request.json.get('login')
    password = request.json.get('password')
    if len(query_postgres('SELECT * FROM Users WHERE username =' + login)) > 0:
        return 'Username already exists'
    
    #create the new database for the user, from functions.py
    #initialize_email()

    query_postgres('INSERT INTO Users (user_id, username, password) VALUES (1,' + login + ',' + password +' )')
    return 'OK'

@app.route('/login', methods=['POST'])
def login():
    # Get the login and password from the request body
    login = request.json.get('login')
    password = request.json.get('password')

    print(login)

    # Perform the database query
    # Replace this with your actual database query logic

    password_true = query_postgres('SELECT password FROM Users WHERE username = "test"')
    if login == "test" and password == password_true:
        print('Login success')
        return jsonify({'success': True})
    else:
        print('Login failed')
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run()
