CREATE DATABASE mindsdb_gmail
WITH ENGINE = 'gmail',
parameters = {
    "credentials_file": "/credentials.json",
    "scopes": [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.insert',
    'https://www.googleapis.com/auth/gmail.labels'
]
};
https://mail.google.com/

'''https://developers.google.com/gmail/api/auth/scopes'''


INSERT INTO mindsdb_gmail.emails (thread_id, message_id, to_email, subject, body)
VALUES ('187cbdd861350934d', '8e54ccfd-abd0-756b-a12e-f7bc95ebc75b@Spark', 'arohan19@gmail.com', 'Trying out MindsDB',
        'This seems awesome. You must try it out whenever you can.');

