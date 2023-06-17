CREATE DATABASE mindsdb_gmail
WITH ENGINE = 'gmail',
parameters = {
    "credentials_file": "mindsdb/integrations/handlers/gmail_handler/credentials.json",
    "scopes": ['https://.../gmail.compose', 'https://.../gmail.readonly', ...]
};
