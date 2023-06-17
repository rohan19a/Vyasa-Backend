import requests 

url = 'http://127.0.0.1:47334/api/sql/query'

headers = {
    "Content-Type": "application/json",
    #"Cookie": "{session=273trgsehgrui3i2riurwehe}"
}
data = {
    "query": "SELECT * FROM example_data.airline_passenger_satisfaction;;"
}

response = requests.post(url, headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")


