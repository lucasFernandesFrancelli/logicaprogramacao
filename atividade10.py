def exercicio01():
  num = int(input("Insira o numero: "))
  i=0
  while i <= num:
    if i%5 == 0 and i%2 != 0: 
     print(i)
    i+=1

def exercicio02():
  num_entradas = int(input("Insira o numero de elementos da lista: "))
  lista = []

  for num in range (num_entradas):
    lista.append(input())
  return lista

def exercicio03(lista):
  contador=0
  for num in lista:
    if num > 5:
      contador+=1
  return contador

def exercicio04():
  menu = {
  'a': "PSG",
  'b' : "BAYERN",
  }
  opcao = input()
  while opcao != 'd':
    if opcao in menu:
      print(menu[opcao])
    opcao = input()
