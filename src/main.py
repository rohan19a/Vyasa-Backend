import mindsdb_sdk

# connects to the default port (47334) on localhost 
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

mysql_demo_db = server.create_database(
    engine = "mysql",
    name = "mysql_demo_db",
    connection_args = {
      "user": "user",
      "password": "MindsDBUser123!",
      "host": "db-demo-data.cwoyhfn6bzs0.us-east-1.rds.amazonaws.com",
      "port": "3306",
      "database": "public"
    }
)
