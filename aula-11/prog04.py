import os
os.system("cls")

# mostrar a média

v = [45, -89, 32, -12, 33]

soma = 0
for elem in v:
    soma = soma + elem
media = soma / len(v)
print(media)