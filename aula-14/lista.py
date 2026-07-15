import os
os.system("cls")

# lista - conteudo heterogênio (qualquer tipo), tamanho dinâmico (pode mudar a execução do programa)

# iniciar uma lista com valores

print("Lista")

lista = ["Ana", 45, 3.2, True, 66]

print(lista)

for indice in range(0, 5, 1):
    print(f"V [{indice}] = {lista[indice]}")

for elemento in lista:
    print(elemento)

# Métodos de manipulação de lista

print("\nLista")
# list() - inicializa uma lista vazia
lista = list() # ou lista = []
print(lista)

# . append adiciona um elemento na lista
print("\nAppend")
lista.append("Ana")
lista.append(4.5)
lista.append(False)
# elemento = input("Elemento: ")
lista.append(elemento)
print(lista)

# insert(indice, elemento) - insere um elemetno em uma posição
print("\nInset")
lista = ["Ana", 34, 5.5, True, 55]
print(lista)
lista.insert(1, "Novo")
print(lista)

# pop(<indice>) - remove um elemento da lista. Lista() remove o ultimo. (indice) remove o indice
print("\nPop")
lista = ["Ana", 34, 5.5, True, 55]
print(lista)
lista.pop() # remove o último
print(lista)
removido = lista.pop(0) # remove o indice 0
print(lista)
print(removido)

# remove(elemento) - remove um elemento especifico
print("\nRemove")
lista = ["Ana", 34, 5.5, True, 55]
print(lista)
lista.remove("Ana") # da erro em elemento que não existe
print(lista)

# index(elemento) - retorna o indice do elemento especificado
print("\nIndex")
lista = ["Ana", 34, 5.5, True, 55]
print(lista)
indice = lista.index(5.5) # não aceita elemento que não existe
print(indice)

# count(elemento) - conta elementos especificados
print("\nCount")
lista = ["Ana", 34, 5.5, True, 55, 34, 34]
print(lista)
elemento = "Ana"
qtd = lista.count(elemento)
print(f"Existe {qtd} {elemento} na lista")

# exemplo
print("\nExemplo")
lista = ["Ana", 34, 5.5, True, 55]
print(lista)
elemento = "Abroba"
if lista.count(elemento) == 0:
    print(f"O elemento {elemento} não existe na lista")
else:
    indice = lista.index(elemento)
    print(f"O elemento {elemento} está na posição {indice}")