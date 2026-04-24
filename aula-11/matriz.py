import os
os.system("cls")
# coluna e linha
matriz = [ # coluna
    [10, 20, 30], # linha
    [40, 50, 60]
]

# percorre toda a matriz
for linha in range(0, 2, 1): # tem duas linhas, e vai de zero a 1
    for coluna in range(0, 3, 1): # para cada volta da linha, passara por três volunas
        print(matriz[linha][coluna], end=" ")
    print()


for linha in matriz: # entende as linhas, ele repete o laço pela quantidade da linha
    for elem in linha: # mostra os elementos dentro da linha
        print(elem, end=" ")
    print()