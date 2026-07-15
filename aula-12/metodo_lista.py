import os
os.system("cls")

# tudo que um objeto pode executar é um método

# métodos/funções de lista

# list() - cria uma lista vazia
lista = list()
print(lista)

# append(elemento) - adiciona um elemento na lista
lista.append("Ana")
elem = 51
lista.append(elem)
lista.append(33)
lista.append(45.6)
# elem = input("Elemento: ")
# lista.append(elem)
print(lista) # ele adiciona na lista mais elementos, adiciona um novo

# insert(posição, elemento) - adiciona um elemento em uma posição da lista
lista.insert(1, "Novo")
print(lista)

# pop([posição]) - remove um elemento [] - é opcional, remove o ultimo elemento ou a [posição]
lista.pop()
print(lista)
removido = lista.pop(2) # se for uma posição que não existe, ele da erro
print(lista, removido)

# remove(elemento) - remove pelo elemento
lista = ['Ana', 'Novo', 51, 33, 45.6]
lista.remove(51) # se for um elemento que não existe, ele da erro
print(lista)

# index() - retorna o indice do elemento
lista = ['Ana', 'Novo', 51, 33, 45.6]
indice = lista.index(51)  # se for um elemento que não existe, ele da erro
print(f"Indice = {indice}")

# count(elemento) - conta quantos elementos especificos existem
lista = ['Ana', 'Novo', 51, 33, 45.6]
quantidade = lista.count(51) # ele trás um resultado mesmo se não tiver um elemento. Uma boa prática é usar count antes
print(f"Quantidade = {quantidade}")

# exemplo
lista = ['Ana', 'Novo', 51, 33, 45.6]
elem = 51

if lista.count(elem) == 0:
    print(f"O elemento {elem} não existe")
else:
    indice = lista.index(elem)
    print(f"O elemento {elem} existe e está no indice {indice}")

# len(objeto) - conta quantos elementos/posições existem em um objeto
lista = ['Ana', 'Novo', 51, 33, 45.6]
quantidade = len("Ana") # conta a quantidade de letras
print(quantidade)
quantidade = len(lista)
print(quantidade)

# sum(objeto númerico) - soma os elementos de um vetor númerico, cuidado com elementos não númericos
lista = [34, 45, 65, -4, 6.6, 5.88]
soma = sum(lista)
print(soma)

# importante saber
soma = 0
for elem in lista: # percorre toda a lista
    soma = soma + elem

print(soma)

# + - concatenação de lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")
print(f"Lista 3 = {lista3}")

# extended(lista) - adiciona uma lista no final da outra
lista1 = [1, 2, 3]
print(f"Lista 1 = {lista1}")
lista2 = [4, 5, 6]
print(f"Lista 2 = {lista2}")
lista1.extend(lista2)
print(f"Lista 2 = {lista1}")

# copy()

lista1 = [1, 2, 3]
lista2 = lista1.copy()
# lista2 = lista1 # não faça assim para copiar, por ter igualado, elas usam o mesmo endereço, então pode repitir
print(lista1)
print(lista2)
lista1.append(4)
print(lista1)
print(lista2)

# sort() - ordena uma lista numerica
lista = [34, 45, 65, -4, 6.6, 5.88]
print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True) # ordem decrescente
print(lista)

# reverse() - inverte as posições
lista = [34, 45, 65, -4, 6.6, 5.88]
lista.reverse()
print(lista)

# clear() - apaga todos os elementos
lista = [34, 45, 65, -4, 6.6, 5.88]
print(lista)
lista.clear()
print(lista)

# del - exclui o objeto da memória
lista = [34, 45, 65, -4, 6.6, 5.88]
print(lista)
del lista[1] # se usar del lista, ele exclui da mémoria
print(lista)