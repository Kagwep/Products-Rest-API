import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/producst/1/"

#emulate http request
get_response = requests.get(endpoint) # Application programming interface

print(get_response.text) # print raw text
print(get_response.json()) 
# javascript object notation
print(get_response.status_code)

