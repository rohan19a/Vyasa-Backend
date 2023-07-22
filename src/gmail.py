from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import time


def gmail_send_message(recipient, sender, subject, message):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )
    creds = flow.run_local_server(port=0)


    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content(message)

        message['To'] = recipient
        message['From'] = sender
        message['Subject'] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def watch_new_emails():
    # Set up credentials
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/gmail.readonly']
    )
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    
    # Create a watch request
    watch_request = {
        'labelIds': ['INBOX'],
        'topicName': 'projects/YOUR_PROJECT_ID/topics/YOUR_TOPIC_NAME'
    }
    response = service.users().watch(userId='me', body=watch_request).execute()
    print('Watch request sent. Waiting for new emails...')

    # Wait for new email notifications
    while True:
        time.sleep(10)  # Adjust the polling interval as desired
        messages = service.users().messages().list(userId='me', q='is:unread').execute()
        if 'messages' in messages:
            for message in messages['messages']:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                raw_data = msg['raw']
                msg_data = base64.urlsafe_b64decode(raw_data).decode('utf-8')
                print(f'New email:\n{msg_data}')
                # Mark the email as read if desired
                # service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()
                return msg_data

if __name__ == '__main__':
    watch_new_emails()
