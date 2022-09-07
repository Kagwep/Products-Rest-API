import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/producst/4/update/"


data = {
    "title" : "Hello there kagwe",
    "price" : 12.88
}
#emulate http request
get_response = requests.put(endpoint,json=data)
#print(get_response.text) # print raw text
print(get_response.json()) 
# javascript object notation
#print(get_response.status_code)

