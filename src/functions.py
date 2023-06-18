import mindsdb_sdk
from queries import make_query
from flask import jsonify

# connects to the default port (47334) on localhost 
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

print(server.list_databases())
my_table = server.get_database('mindsdb_gmail')
print(my_table.list_tables())

def decide(body):
    return 0


def initialize_email():
    quer = '''
    CREATE DATABASE mindsdb_gmail
    WITH ENGINE = 'gmail',
    parameters = {
        "credentials_file": "credentials.json",
        "scopes": [
        'https://www.googleapis.com/auth/gmail.readonly'
        ]
    };
    '''

    server.query(quer)

def update_minds(table):
    server.get_database('users').get_table(table).update()
    return jsonify({'success': True})