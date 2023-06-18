from queries import query_postgres, insert_into_users
from flask import jsonify, request, Flask, request
import json
from dotenv import load_dotenv
import os
load_dotenv()
import requests


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

@app.route('/demo', methods=['OPTIONS'])
def handle_demo_options():
    response_headers = {
        'Access-Control-Allow-Origin': '*',  # Replace '*' with the actual allowed origin(s)
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    return ('', 204, response_headers)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        if 'username' in data and 'password' in data:
            username = data['username']
            password = data['password']
            query_postgres(f"UPDATE users SET password = '{password}' WHERE username = '{username}'")
            return jsonify({'message': 'Password updated successfully'}), 200
        else:
            return jsonify({'message': 'Username and password are required'}), 400
    else:
        return jsonify({'message': 'Method not allowed'}), 405

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
    data = request.get_json(force=True)
    email_address = data['email_address']

    query_postgres('DELETE FROM EmailAddresses WHERE email_id = ' + email_address)
    return 'OK'

@app.route('/create', methods=['PUT'])
def create():
    data = request.get_json(force=True)
    user_id = data['user_id']
    email_id = data['email_id']
    email_address = data['email_address']
    query_postgres(f"INSERT INTO EmailAddresses (user_id, email_id, email_address) VALUES ('{user_id}', '{email_id}', '{email_address}')")
    return json.dumps({'success': True})

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

@app.route('/demo', methods=['POST'])
def demo():
    data = request.json
    messages = data['messages']
    print(data)


    # Construct the payload
    payload = {
        'messages': messages
    }

    # Make a POST request to the ChatGPT API
    response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers={
        'Authorization': '',
        'Content-Type': 'application/json'
    })
    print(response.json())

    # Parse the response
    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({'error': 'Something went wrong.'}), 500    

if __name__ == '__main__':
    app.run()
