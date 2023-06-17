import mindsdb_sdk
from queries import make_query

# connects to the default port (47334) on localhost 
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')












#https://docs.mindsdb.com/sql/project
#project = server.get_project()

#make_query('CREATE DATABASE project_alpha;')

#make_query('SHOW FULL DATABASES;')


#print(project.list_models())

'''
my_model = project.create_model (
    name = 'my_model',
    predict = 'target',
    query = my_table
)
'''