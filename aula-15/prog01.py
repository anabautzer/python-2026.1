import os
os.system("cls")

print("Digite os valores ou . para terminar:")

lista = list()
while True:
    entrada = input()
    if entrada == ".":
        break
    else:
        lista.append(float(entrada))

print(f"Lista original: {lista}")
lc = lista.copy()
lc.sort()
print(f"Lista crescente: {lc}")
ld = lista.copy()
ld.sort(reverse=True)
print(f"Lista decrescente: {ld}")
li = lista.copy()
li.reverse()
print(f"Lista invertida: {li}")


