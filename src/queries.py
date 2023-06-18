import requests 
import psycopg2

url = 'http://127.0.0.1:47334/api/sql/query'

def make_query(query):
    cookies = {'session': '273trgsehgrui3i2riurwehe'}
    resp = requests.post(url, json={'query': query}, cookies=cookies)
    if resp.status_code != 200:
        raise Exception('Query failed')
    return resp.json()

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
