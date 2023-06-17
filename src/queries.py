import requests 

url = 'http://127.0.0.1:47334/api/sql/query'

def make_query(query):
    cookies = {'session': '273trgsehgrui3i2riurwehe'}
    resp = requests.post(url, json={'query': query}, cookies=cookies)
    if resp.status_code != 200:
        raise Exception('Query failed')
    return resp.json()

