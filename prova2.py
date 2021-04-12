def exercicio1(nota1, nota2, nota3):
  media = 0
  media = float((nota1+nota2+nota3)/3)
  return (f"A media do aluno é: {media}")
  

def exercicio2():
  num_elementos = int(input("Insira o numero de elementos da lista: "))
  lista = []

  for num in range (num_elementos):
    lista.append(input())
  return lista


def exercicio3():
  menu = {
  'a': "globo",
  'b' : "sbt",
  }
  opcao = input()
  while opcao != 'z' and opcao != 'Z':
    if opcao in menu:
      print(menu[opcao])
    else:
      print("Inválido")
    opcao = input()

def exercicio4(lista):
  media_inferior_a_7 = 0
  porcentagem = len(lista) * 0.25
  for media in lista:
    if media < 7:
      media_inferior_a_7 += 1
  if media_inferior_a_7 < porcentagem:
    return 'Professor coxa'
  else:
    return "Professor padrão"
