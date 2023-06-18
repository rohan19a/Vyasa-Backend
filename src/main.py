import mindsdb_sdk

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

s = server.list_databases()
print(s)
s = server.list_projects()
print(s)

prod = server.get_project('prod')

my_model = prod.list_models()
print(my_model)