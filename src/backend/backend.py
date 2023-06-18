from queries import query_postgres, insert_into_users
from flask import jsonify, request, Flask
import json



app = Flask(__name__)

@app.route('/signup', methods=['OPTIONS'])
def handle_signup_options():
    response_headers = {
        'Access-Control-Allow-Origin': '*',  # Replace '*' with the actual allowed origin(s)
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    return ('', 204, response_headers)

@app.route('/login', methods=['OPTIONS'])
def handle_login_options():
    response_headers = {
        'Access-Control-Allow-Origin': '*',  # Replace '*' with the actual allowed origin(s)
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    return ('', 204, response_headers)

@app.route('/update', methods=['POST'])
def update():
    query_postgres('INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (1, "test", "test")')
    query_postgres('ISERT INTO EmailAttributes (attribute_id, email_id, name, role, description, authority, department), VALUES (1, 1, "test", "test", "test", "test", "test")')
    return 'OK'

@app.route('/get', methods=['GET'])
def get():
    content = request.get_json(silent=True)
    login = content['username']

    user_id = query_postgres('SELECT user_id FROM Users WHERE username =' + login)
    if len(user_id) == 0:
        return 'Username does not exist'
    id = query_postgres('SELECT email_id FROM EmailAddresses WHERE user_id =' + user_id)
    if len(id) == 0:
        return 'No emails'
    q = query_postgres('SELECT * FROM EmailAttributes where EmailAttributes.email_id =' + id)
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

    content = request.get_json(silent=True)
    login = content['username']
    password = content['password']

    print(content)

    if len(query_postgres(f"SELECT * FROM users WHERE username = '{login}'")) > 0:
        return jsonify({'success': False, 'error': 'Username already exists'})

    id = ""
    for x in login:
        if x.isnumeric():
            id += str(x)
        else:
            id += str(ord(x))

    id = str(int(id) % 123445)


    insert_into_users(id, login, password)    

    return json.dumps({'success': True})

@app.route('/login', methods=['POST'])
def login():
    # Get the login and password from the request body
    content = request.get_json(silent=True)
    login = content['username']
    password = content['password']

    print(content)

    # Perform the database query
    # Replace this with your actual database query logic

    password_true = query_postgres('SELECT password FROM users WHERE username = ' + login + ')')
    if password == password_true:
        print('Login success')
        return jsonify({'success': True})
    else:
        print('Login failed')
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run()
