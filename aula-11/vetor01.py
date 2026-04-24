import os
os.system("cls")

# criando um "vetor", iniciando com um valor
# saber que os indices existem (0 1 2 3 4)
# como fazer para pegar o primeiro e o último - indices negativos (-5 -4 -3 -2 -1)
v = [45, 56, 76, -45, 34, 44, 55]

print(v)
print(v[0])
print(v[4])
print(v[-1])

print(len(v)) # retorna a quantidade de elementos (no caso, 7)
print(len("Ana Carolina"))

for ind in range(0, len(v), 1):
    print(ind, v[ind]) # traz o número do indice e o conteúdo

for ind, elem in enumerate(v): # mostra o valor do elemento, respitando o indice
    print(f" {ind} - {elem}", end=" | ")

for elem in enumerate(v): # mostra o valor do elemento, respitando o indice
    print(elem, end=" ")