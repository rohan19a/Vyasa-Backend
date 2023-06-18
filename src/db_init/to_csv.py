import psycopg2
import csv
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

query = """
    select *
    from users
"""
outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
with open('archivo.csv', 'w') as f:
    cur.copy_expert(outputquery, f)
conn.close()
