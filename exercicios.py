def minimo_3(n1,n2,n3):
  if n1 < n2 and n1 < n3 :
    return n1 
  elif n2 < n3 :
      return n2
  return n3
  
print(minimo_3 (4,8,2))

--------------------------------------

def meu_minimo (lista):
  minimo = lista[0]
  for elemento in lista:
    if elemento < minimo:
      minimo = elemento 
  return minimo

------------------------------------------

def minha_soma(lista):
  soma=0
  for elemento in lista:
    soma+=elemento
  return soma

------------------------------------------

def meu_sort(lista):
  tam=len(lista)
  for i in range(tam):
    for j in range(i + 1, tam):
      if lista[i] > lista[j]:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
  return lista
------------------------------------------

def meu_sort(lista):
  tam=len(lista)
  for i in range(tam):
    for j in range(i + 1, tam):
      if lista[i] > lista[j]:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
  return lista

----------------------------------------

def minha_soma(lista):
  soma=0
  for elemento in lista:
    soma+=elemento
  return soma
  
lista=[4,5,0,7,9,5]
sort = meu_sort(lista)
minimos = sort[:2]
media = minha_soma(minimos)/2
print(media)

-------------------------------------

def cria_matriz(nlinhas,ncolunas):
  matriz=[]
  for i in range(nlinhas):
    linha = []
    for j in range (ncolunas):
      linha.append(0)
    matriz.append(linha)
  return matriz

def imprime_matriz(matriz):
  for i in range(len(matriz)):
    linha = matriz[i]
    for j in range(len(linha)):
      print(matriz[i][j], end=" ")
    print()
  

matriz = cria_matriz(5,4)
imprime_matriz(matriz
