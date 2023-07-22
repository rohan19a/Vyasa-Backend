#get the most recent emails to the user from a postgres database, if the emails haven't already been checked, then apply a function on them which calls open ai api on them as a prompt
#and then return the response from the api

import os
import sys
import json
import requests
import datetime
import time
import psycopg2
import openai #import openai


from gmail import watch_new_emails




psycopg2.connect(
    host = os.environ['DB_HOST'],
    database = os.environ['DB_NAME'],
    user = os.environ['DB_USER'],
    password = os.environ['DB_PASSWORD']
)

def get_recent_emails(user_id):
    msg = watch_new_emails
    

    return []

def chatgpt(msg):
    #call the open ai api on the message
    #return the response


