from queries import query_postgres, insert_into_users
from flask import jsonify, request, Flask, request
import json
from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


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
            query_postgres(f"UPDATE Users SET password = '{password}' WHERE corporate_email = '{username}'")
            return jsonify({'message': 'Password updated successfully'}), 200
        else:
            return jsonify({'message': 'Username and password are required'}), 400
    else:
        return jsonify({'message': 'Method not allowed'}), 405

@app.route('/get', methods=['GET'])
def get():
    content = request.get_json(silent=True)
    login = content['username']

    user_id = query_postgres(f"SELECT user_id FROM Users WHERE corporate_email = '{login}'")
    if len(user_id) == 0:
        return 'Username does not exist'
    q = query_postgres(f"SELECT * FROM EmailAttributes where EmailAttributes.corporate_email = '{login}'")
    return 'OK'

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json(force=True)
    email_address = data['email_address']

    query_postgres(f"DELETE FROM EmailAddresses WHERE email_address = '{email_address}'")
    return 'OK'

@app.route('/create', methods=['PUT'])
def create():
    data = request.get_json(force=True)
    email_id = data['email_id']
    email_address = data['email_address']

    query_postgres(f"INSERT INTO EmailAddresses (email_id, email_address) VALUES ('{email_id}', '{email_address}')")
    return json.dumps({'success': True})

@app.route('/signup', methods=['POST'])
def signup():

    content = request.get_json(silent=True)
    login = content['username']
    password = content['password']

    print(content)

    if len(query_postgres(f"SELECT * FROM Users WHERE corporate_email = '{login}'")) > 0:
        return jsonify({'success': False, 'error': 'Username already exists'})


    insert_into_users(login, password)    

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

    password_true = query_postgres(f"SELECT password FROM Users WHERE corporate_email = '{login}'")
    if password == password_true:
        print('Login success')
        return jsonify({'success': True})
    else:
        print('Login failed')
        return jsonify({'success': False})

@app.route('/demo', methods=['POST'])
def demo():
    data = request.json
    print(data)

    mess = data['messages']
    for message in mess:
        content = message['content']
        message_id = message.get('email_id')

    prompt = "The first part of the following prompt is an email from a customer or interested party to a corporation's email. The second part is a list of members of this corporation with a list of their emails and a description of their jobs. Select the best person to send the email to: This is the user email: "
    if message_id is not None:
        print(query_to_list(message_id))
    message = prompt + content + '. And this is the list of corporate worker entities: '
    print(message)

    # Make a POST request to the ChatGPT API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': 'hello'}],
        )
    
    print(completion.choices[0].message)
    

    # Parse the response
    if completion is not None:
        return jsonify(completion.choices[0].message), 200
    else:
        return jsonify({'error': 'Something went wrong.'}), 500    

def query_to_list(corporate_email):
    result = query_postgres("SELECT * FROM EmailAttributes;")
    print(result)

if __name__ == '__main__':
    app.run()
