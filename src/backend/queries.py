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

''''
insert_into_users("info@general_cooperation.com", "test")
insert_into_EmailAttributes("info@general_cooperation.com", "joe@general_cooperation.com", "Joe", "Developer", "Website developer", "Intern", "Technology")
insert_into_EmailAttributes("info@general_cooperation.com", "mike@general_cooperation.com", "Mike", "CEO", "CEO of General Cooperation", "C-Suite", "Management")
insert_into_EmailAttributes("info@general_cooperation.com", "rohan@general_cooperation.com", "Rohan", "CTO", "CTO of General Cooperation", "C-Suite", "Technology")
insert_into_EmailAttributes("info@general_cooperation.com", "james@general_cooperation.com", "James", "CFO", "CFO of General Cooperation", "C-Suite", "Management")
insert_into_EmailAttributes("info@general_cooperation.com", "jane@general_cooperation.com", "Jane", "Developer", "Website developer", "Medium Authority", "Technology")

'''
















qqq = '''

CREATE TABLE EmailAddresses (
  corporate_email VARCHAR(255),
  email_address VARCHAR(255),
  PRIMARY KEY (corporate_email),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE EmailAttributes (
  corporate_email VARCHAR(255),
  name VARCHAR(255),
  role VARCHAR(255),
  description VARCHAR(255),
  authority VARCHAR(255),
  department VARCHAR(255),
  FOREIGN KEY (corporate_email) REFERENCES EmailAddresses(corporate_email)
);
'''













'''
insert_into_users(10, "info@general_cooperation.com", "test")
insert_into_EmailAddresses(3, 10, "mike@general_cooperation.com")
insert_into_emailAttributes(1, info@general_cooperation.com, "Mike", "CEO", "CEO of General Cooperation", "C-Suite", "Management")

insert_into_EmailAddresses(4, 10, "rohan@general_cooperation.com")
insert_into_emailAttributes(2, info@general_cooperation.com, "Rohan", "CTO", "CTO of General Cooperation", "C-Suite", "Technology")

insert_into_EmailAddresses(5, 10, "james@general_cooperation.com")
insert_into_emailAttributes(3, info@general_cooperation.com, "James", "CFO", "CFO of General Cooperation", "C-Suite", "Managment")

insert_into_EmailAddresses(6, 10, "jane@general_cooperation.com")
insert_into_emailAttributes(4, info@general_cooperation.com, "Jane", "Deverloper", "Website developer", "Medium Authority", "Technology")

insert_into_EmailAddresses(7, 10, "joe@general_cooperation.com")
insert_into_emailAttributes(5, info@general_cooperation.com, "Joe", "Deverloper", "Website developer", "Intern", "Technology")
'''


import random

querier = [
    ['sender1@example.com', 'customer1@example.com', 'Regarding your offerings', "Hi there! Im interested in learning more about your product line. Can you please provide details about the nutritional value of your baby food products?"],
    ['sender2@example.com', 'customer2@example.com', 'Inquiry about your services', "Hello! Im curious to know more about the services your business offers. Could you please explain the battery life and charging capabilities of your phone batteries?"],
    ['sender3@example.com', 'customer3@example.com', 'Question about your company', "Greetings! Ive heard great things about your company and Im wondering if your bicycles come with adjustable seat heights. Can you provide more information about this feature?"],
    ['sender4@example.com', 'customer4@example.com', 'Seeking information', "Good day! Im conducting research on different businesses and I would appreciate it if you could provide specific details about the materials used in your baby food packaging"],
    ['sender5@example.com', 'customer5@example.com', 'Inquiry about your products', "Hi! Im specifically interested in your range of phone batteries. Can you tell me if they are compatible with both Android and iOS devices?"],
    ['sender6@example.com', 'customer6@example.com', 'Exploring partnership opportunities', "Hello! I represent a local retail store and Im interested in stocking your bicycles. Can you please provide information on wholesale pricing and minimum order quantities?"],
    ['sender7@example.com', 'customer7@example.com', 'Question about your services', "Good day! Im considering using your repair services for bicycles. Can you let me know if you offer pick-up and drop-off options for repairs?"],
    ['sender8@example.com', 'customer8@example.com', 'Looking for information', "Hi there! Im currently in the market for a new bike and Id like to know if your company offers any customization options such as frame color and accessories"],
    ['sender9@example.com', 'customer9@example.com', 'Inquiry about your company', "Hello! Im conducting market research and Im curious to know if your company uses sustainable and eco-friendly practices in the production of your baby food."],
    ['sender10@example.com', 'customer10@example.com', 'Interested in your offerings', "Hi! Im interested in your range of phone accessories. Can you provide specific details about the compatibility of your products with the latest smartphone models?"],
    ['sender11@example.com', 'customer11@example.com', 'Question about your services', "Greetings! Im interested in your bike rental services. Can you please clarify if helmets and locks are included with the rental, or if they are available for an additional fee?"],
    ['sender12@example.com', 'customer12@example.com', 'Inquiry about your company', "Good day! Im fascinated by your companys commitment to sustainability. Can you provide specific details about the steps you take to reduce your carbon footprint?"],
    ['sender13@example.com', 'customer13@example.com', 'Seeking information', "Hello! Im looking to purchase baby food in bulk quantities for a nonprofit organization. Can you provide specific information about the shelf life and storage recommendations for your products?"]
]


inaa = 0
for x in querier:
    inaa += 1
    insert_into_EmailMessages('info@general_cooperation.com', x[1], x[2])


