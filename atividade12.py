from random import randint
from random import random
#exibir o maior entre três variaveis

num1 = int(input())
num2 = int(input())
num3 = int(input())
maior = num1

if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior=num3

print(maior)



print(list("Eu sou um aluno feliz".split())) #transforma o texto em uma lista de palavras

#calcula a soma da lista

lista = [3, 6, 3, 2, 1]
print(sum(lista))


#transforma uma lista de palavras emm uma frase

lista = ["seu", "joao", "esta", "aqui"]

print(str.join(' ',lista))




lista_numeros = [3, 8, 9, 1, 0, 2]

print(list(filter(lambda x: x%2 == 0, lista_numeros)))#imprimir lista dos elementos pares da lista

print(sum(filter(lambda x: x >= 4, lista_numeros)))

print(sum(lista_numeros)/len(lista_numeros))

print(str.join('|',map(lambda x: str(x), lista_numeros)))

print(sorted(lista_numeros))

print(sorted(lista_numeros, reverse=True))


lista_numeros = [4, 5, 2, 0, 9]

print(lista_numeros[:])

print(lista_numeros[:3])

print(sorted(lista_numeros)[:2])

print(sorted(lista_numeros)[-3:])


print([x+1 for x in range(10)])

print( [x*2 for x in range(11)] )

print( [randint(1, 30) for x in range(20)] )



lista = ["alo", "Alo", "aLO", "alO"]
print(list(map(lambda x: x.upper(), lista)))

lista = ["alo", "Alo", "aLO", "alO"]
print(list(map(lambda x: x.lower(), lista)))
