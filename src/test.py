from queries import query_postgres

query_postgres('SELECT password FROM Users WHERE username = "test20"')