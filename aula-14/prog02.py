import os
os.system("cls")

# fazer um programa que inicialize vazia

lista = list()
print(lista)


while True:
    elem = input("Digite elementos: ")
    if elem == ".":
        break
    else:
        lista.append(elem)

print(lista)

listanum = []
listraoutro = []
for item in lista:
    if item.isnumeric():
        listanum.append(int(item))
    else:
        listraoutro.append(item)

print(listanum)
print(listraoutro)
