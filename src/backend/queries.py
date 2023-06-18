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
    try:
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

    # Commit the changes to the database
        conn.commit()


    except psycopg2.Error as e:
        print("Error creating tables:", e)

    finally:
    # Close the cursor and database connection
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_into_users(user_id, user_name, user_password):
      with conn.cursor() as cur:
          cur.execute("INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)", (user_id, user_name, user_password))
          conn.commit()
          cur.close()

def insert_into_EmailAddresses(email_id, user_id, email_address):
      with conn.cursor() as cur:
          cur.execute("INSERT INTO EmailAddresses (email_id, user_id, email_address) VALUES (%s, %s, %s)", (email_id, user_id, email_address))
          conn.commit()
          cur.close()

def insert_into_emailAttributes(attribute_id, email_id, name, role, description, authority, department):
  with conn.cursor() as cur:
      cur.execute("INSERT INTO EmailAttributes (attribute_id, email_id, name, role, description, authority, department) VALUES (%s, %s, %s, %s, %s, %s, %s)", (attribute_id, email_id, name, role, description, authority, department))
      conn.commit()
      cur.close()