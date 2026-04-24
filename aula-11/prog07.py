import os
os.system("cls")

# mostrar os pares

v = [45, 56, 76, -45, 34]

for ind in range( 0, len(v), 1):
    if ind % 2 == 0:
        print(v[ind], end=" ")

for i in range( 0, len(v), 2): # outro jeito de fazer
    print(v[i])