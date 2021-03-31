def converte_entrada(texto):
  converte = texto.split()
  lista=[]
  for num in converte:
    lista.append(int(num))
  return lista

  
def processa_numeros(texto):
  soma=0
  for num in texto:
    soma += num
  return (soma, len(texto))


def main(soma_e_indice):
  soma = soma_e_indice[0]
  indice = soma_e_indice[1]
  media = soma/indice
  return media
  
  
txt=converte_entrada((input()))  
processa=processa_numeros(txt)
principal=main(processa)
print(principal)
