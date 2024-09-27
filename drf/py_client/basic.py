import requests 

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={'secret_key':'134sdf234df'}, json = {"name":"G.O.A.T"}) 

print(get_response.json())
# print(get_response.text)
print(get_response.status_code)


