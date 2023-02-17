import requests
from pprint import pprint


#Get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
# pprint(resultado_get.json())

#Get com id
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_com_id.json())

#   POST criar um novo recurso 
nova_funcao = {'completed': False,
 'title': 'testar api',
 'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_funcao)
#pprint(resultado_post.json())

#Put - alterar um recurso existente 
tarefa_alterada = {'completed': False,
 'title': 'testando alterada api',
 'userId': 1}

resultado_pu = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
#pprint(resultado_pu.json())

#DELETE - Para deletar uma recurso 

funcao_deletada = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(funcao_deletada.json())