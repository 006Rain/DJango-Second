import requests, pprint, json

user_info = { "username": "admin", "password": "admin" }

response = requests.post( "http://127.0.0.1:8000/mgr/signin/", data=user_info )
pprint.pprint( response.json() )

params = { "action":"list_customer", }
response = requests.get( "http://127.0.0.1:8000/mgr/customers/", params=params )
pprint.pprint( response.json() )