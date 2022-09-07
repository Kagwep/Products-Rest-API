import requests

product_id = input('Delete product: \n')

try :
    product_id = int(product_id)
except:
    print("Invalid")
    

if product_id:
    #endpoint = "https://httpbin.org/status/200/"
    #endpoint = "https://httpbin.org/anything"
    endpoint = f" http://localhost:8000/api/producst/{product_id}/destroy/"

    #emulate http request
    get_response = requests.delete(endpoint)
    #print(get_response.text) # print raw text
    print(get_response.status_code) 
    # javascript object notation
    #print(get_response.status_code)