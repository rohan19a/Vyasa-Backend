import mindsdb_sdk

# connects to the default port (47334) on localhost 
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

server.list_databases()
my_table = server.get_database('mindsdb_gmail')

print(my_table.list_tables())

email = my_table.get_table('emails')
#print(email.fetch())

query = '''
CREATE MODEL text_summarization_model
PREDICT highlights
USING
    engine = 'openai',              
    prompt_template = 'provide an informative summary of the text text:{{article}} using full sentences';
'''

print(query)