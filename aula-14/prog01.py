import os
os.system("cls")

# fazer um programa que inicialize vazia

lista = list()
print(lista)


while True:
    elem = input("Digite elementos: ")
    if elem == ".":
        break
    # if elem.isnumeric():
    #     lista.append(float(elem))
    else:
        lista.append(elem)

print(lista)