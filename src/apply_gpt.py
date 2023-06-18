import mindsdb_sdk
from queries import make_query

server = mindsdb_sdk.connect()

emails = server.get_database('mindsdb_gmail')
user_data = server.get_database('user_data')

#get the elements of all tables of user where user_id = 1
user = user_data.query('select * from users where user_id = 1')
messages = user_data.query('select * from emailmessages where user_id = 1')
email = user_data.query('select * from emailaddresses where user_id = 1')
e_attributes = user_data.query('select * from emailattributes where user_id = 1')

#run ChatGPT on the new messages and determine which e_atrributes are most relevent
query = '''
CREATE MODEL prod.openai_test_a
PREDICT answer
USING
    engine = 'openai',
    prompt_template = 'Out of a list of these email atrributes: {{e_attributes}}. return the row that is most related to the message: {{messages}}. Answer:',
    question_column = 'e_attributes',
    api_key = env.OPENAI_API_KEY,;

'''

make_query(query)   
