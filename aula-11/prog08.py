import os
os.system("cls")

# usuario dar um número e ver se tem

v = [45, 56, 76, -45, 34]

busca = int(input("Dê um número: "))
achou = False # flag, controla o programa, começa com falso

for elem in v: # procurar o elemento dentro de v e ver se é igual
    if elem == busca:
        achou = True
        break

if achou:
    print(f"Existe o elemento {busca} no vetor")
else:
    print(f"Não existe o elemento {busca} no vetor")