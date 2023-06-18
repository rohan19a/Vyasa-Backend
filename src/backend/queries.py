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

def insert_into_EmailMessages(message_id, user_id, message_content, timestamp, other_message_attributes):
  with conn.cursor() as cur:
      cur.execute("INSERT INTO EmailMessages (message_id, user_id, message_content, timestamp, other_message_attributes) VALUES (%s, %s, %s, %s, %s)", (message_id, user_id, message_content, timestamp, other_message_attributes))
      conn.commit()
      cur.close()


'''
insert_into_users(10, "info@general_cooperation.com", "test")
insert_into_EmailAddresses(3, 10, "mike@general_cooperation.com")
insert_into_emailAttributes(1, 3, "Mike", "CEO", "CEO of General Cooperation", "C-Suite", "Management")

insert_into_EmailAddresses(4, 10, "rohan@general_cooperation.com")
insert_into_emailAttributes(2, 4, "Rohan", "CTO", "CTO of General Cooperation", "C-Suite", "Technology")

insert_into_EmailAddresses(5, 10, "james@general_cooperation.com")
insert_into_emailAttributes(3, 5, "James", "CFO", "CFO of General Cooperation", "C-Suite", "Managment")

insert_into_EmailAddresses(6, 10, "jane@general_cooperation.com")
insert_into_emailAttributes(4, 6, "Jane", "Deverloper", "Website developer", "Medium Authority", "Technology")

insert_into_EmailAddresses(7, 10, "joe@general_cooperation.com")
insert_into_emailAttributes(5, 7, "Joe", "Deverloper", "Website developer", "Intern", "Technology")
'''


querier = [
    ['customer1@example.com', 'Regarding your offerings', "Hi there! I'm interested in learning more about your product line. Can you please provide details about the nutritional value of your baby food products?"],
    ['customer2@example.com', 'Inquiry about your services', "Hello! I'm curious to know more about the services your business offers. Could you please explain the battery life and charging capabilities of your phone batteries?"],
    ['customer3@example.com', 'Question about your company', "Greetings! I've heard great things about your company and I'm wondering if your bicycles come with adjustable seat heights. Can you provide more information about this feature?"],
    ['customer4@example.com', 'Seeking information', "Good day! I'm conducting research on different businesses and I would appreciate it if you could provide specific details about the materials used in your baby food packaging"],
    ['customer5@example.com', 'Inquiry about your products', "Hi! I'm specifically interested in your range of phone batteries. Can you tell me if they are compatible with both Android and iOS devices?"],
    ['customer6@example.com', 'Exploring partnership opportunities', "Hello! I represent a local retail store and I'm interested in stocking your bicycles. Can you please provide information on wholesale pricing and minimum order quantities?"],
    ['customer7@example.com', 'Question about your services', "Good day! I'm considering using your repair services for bicycles. Can you let me know if you offer pick-up and drop-off options for repairs?"],
    ['customer8@example.com', 'Looking for information', "Hi there! I'm currently in the market for a new bike and I'd like to know if your company offers any customization options such as frame color and accessories"],
    ['customer9@example.com', 'Inquiry about your company', "Hello! I'm conducting market research and I'm curious to know if your company uses sustainable and eco-friendly practices in the production of your baby food."],
    ['customer10@example.com', 'Interested in your offerings', "Hi! I'm interested in your range of phone accessories. Can you provide specific details about the compatibility of your products with the latest smartphone models?"],
    ['customer11@example.com', 'Question about your services', "Greetings! I'm interested in your bike rental services. Can you please clarify if helmets and locks are included with the rental, or if they are available for an additional fee?"],
    ['customer12@example.com', 'Inquiry about your company', "Good day! I'm fascinated by your company's commitment to sustainability. Can you provide specific details about the steps you take to reduce your carbon footprint?"],
    ['customer13@example.com', 'Seeking information', "Hello! I'm looking to purchase baby food in bulk quantities for a nonprofit organization. Can you provide specific information about the shelf life and storage recommendations for your products?"]
]
'''
inaa = 0
for x in querier:
    inaa += 1
    insert_into_EmailMessages(inaa, 10, x[2], "2021-01-01 00:00:00", "test")
    '''