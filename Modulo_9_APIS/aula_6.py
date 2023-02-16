import requests
from pprint import pprint


#Get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
# pprint(resultado_get.json())

#Get com id
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
# pprint(resultado_get_com_id.json())

#   POST criar um novo recurso 

