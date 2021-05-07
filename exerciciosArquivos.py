import os
import requests
import json

#exercicio01
'''
pasta_downloads = os.environ['HOMEPATH'] + '/Downloads'
file = open(pasta_downloads + "/teste.txt", "r")
conteudo = file.read()
file.close()
print(conteudo)
'''
#exercicio02
"""
with open ("./precos.txt", "r") as file:
    precos= list( map ( lambda preco: float(preco.strip("\n")), file.readlines()))
    media = sum(precos) / len(precos)
    file.close()
    print(media)
"""

#exercicio03
"""
with open(os.environ['HOMEPATH']+"/nome.txt", "w") as file:
    for elemento in "Lucas Fernandes Francelli".split():
        file.write(elemento + "\n")
    file.close()
"""

#exercicio04
'''
resposta = requests.get(' https://jsonplaceholder.typicode.com/todos/1')
teste = resposta.text
print(teste)
'''

#exercicio05
'''
resposta = requests.get(' https://jsonplaceholder.typicode.com/todos/1')
dicionario = json.loads(resposta.text)
atributo = dicionario['title']
print(atributo)
'''

#exercicio06
'''
resposta = requests.get('https://jsonplaceholder.typicode.com/posts')
lista = json.loads(resposta.text)

for val in lista:
    print(val["body"]+"\n")
'''

