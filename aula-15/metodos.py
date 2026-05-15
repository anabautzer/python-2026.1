import os
os.system("cls")

#len(objeto) - conta os elementos de um objeto
print("Len()")
nome = "Ana"
qtd = len(nome)
print(qtd)
lista = [45,"Ana", 5.6, 55, True]
qtd = len(lista)
print(qtd)

# sum(numero) - efetua a soma dos elementos numericos na lista
print("\nsum()")
lista = [45, 87, 5.6, 55, 3.45]
soma = sum(lista)
print(soma)

# + - contatenação de lista
print("\nSoma de lista")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

# extend - adiciona uma lista no final da outra
print("\nextend")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)
l1.extend(l2)
print(l1)
print(l2)

# copy() - copiar um objeto
print("\ncopy()")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2 = l1.copy()
print(l1)
print(l2)

#sort() - ordena uma lista do mesmo tipo
print("\nsort()")
lista = [45, 87, 5.6, 55, 3.45]
lista.sort() # o padrão é ordem crescente
print(lista)
lista.sort(reverse=True)
print(lista)

lista2 = ["10", "020", "3"] # ele não ajeita corretamente
lista2.sort()
print(lista2)

#reverse() - inverte a ordem dos elementos
print("\nreverse()")
lista = [45, 87, 5.6, 55, 3.45, "Ana"]
print(lista)
lista.reverse()
print(lista)
