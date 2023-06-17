CREATE DATABASE mindsdb_gmail
WITH ENGINE = 'gmail',
parameters = {
    "credentials_file": "./credentials.json",
    "scopes": ['https://www.googleapis.com/auth/gmail.readonly']
};
