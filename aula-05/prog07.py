import os
os.system ("cls")

# média e mostrar se foi aprovado ou reprovado

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
if media >= 6:
    print(f"Média: {media: .2f} - Aprovado")
else:
    print(f"Média: {media: .2f} - Reprovado")