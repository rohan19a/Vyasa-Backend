import requests 
import psycopg2

url = 'http://127.0.0.1:47334/api/sql/query'
config = 'local'

def make_query(query):
    cookies = {'session': '273trgsehgrui3i2riurwehe'}
    resp = requests.post(url, json={'query': query}, cookies=cookies)
    if resp.status_code != 200:
        raise Exception('Query failed')
    return resp.json()

if config == 'local':
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres"
        )
elif config == 'remote':
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user = "postgres",
        password="postgres"
        )



def query_postgres(query):
    # Connect to the PostgreSQL server
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres"
        )

        # Create a cursor object to execute SQL statements
        cur = conn.cursor()

    # Execute the SQL statements to create tables
        cur.execute(query)

        rows = cur.fetchall()
        


    # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        cur.close()
        conn.close()

        return rows


def insert_into_users(corporate_email, user_password):
    query = "INSERT INTO Users (corporate_email, password) VALUES ('{}', '{}')".format(corporate_email, user_password)
    query_postgres(query)

def insert_into_EmailAttributes(corporate_email, email_address, name, role, description, authority, department):
    query = "INSERT INTO EmailAttributes (corporate_email, email_address, name, role, description, authority, department) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(corporate_email, email_address, name, role, description, authority, department)
    query_postgres(query)

def insert_into_EmailMessages(corporate_email, sender_email, message_content):
    query = "INSERT INTO EmailMessages (corporate_email, sender_email, message_content) VALUES ('{}', '{}', '{}')".format(corporate_email, sender_email, message_content)
    query_postgres(query)