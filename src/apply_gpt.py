import mindsdb_sdk

server = mindsdb_sdk.connect()

emails = server.get_database('mindsdb_gmail')
user_data = server.get_database('users')

#get the elements of all tables of user where user_id = 1
user = user_data.get_table('users').select(['*'], where={'user_id': 1})
messages = user_data.get_table('emailmessages').select(['*'], where={'user_id': 1})
email = user_data.get_table('emailaddresses').select(['*'], where={'user_id': 1})
e_attributes = user_data.get_table('emailattributes').select(['*'], where={'email_id': email[0]['email_id']})

#run ChatGPT on the new messages and determine which e_atrributes are most relevent
query = '''
CREATE MODEL project_a.openai_test_a
PREDICT answer
USING
    engine = 'openai',
    prompt_template = 'Out of a list of these email atrributes: {{e_attributes}}. return the row that is most related to the message: {{messages}}. Answer:',
    question_column = 'e_attributes',
    api_key = env.OPENAI_API_KEY,;

'''

ans = server.query(query)
print(ans)