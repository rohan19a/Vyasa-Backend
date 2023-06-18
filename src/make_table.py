import http.client

conn = http.client.HTTPConnection("127.0.0.1:47334")

conn.request("GET", "/api/projects/prod/tables")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))