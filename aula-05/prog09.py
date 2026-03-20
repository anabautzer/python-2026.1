import os
os.system ("cls")

# se a nota é valida e fazer a média

n1 = float(input("Nota 1: "))
if not (0 <= n1 <= 10):
    print(f"{n1: .2f} é uma nota invalida")
else: 
    n2 = float(input("Nota 2: "))
    if not (0 <= n2 <= 10):
        print(f"{n2: .2f} é uma nota invalida")
    else:  
        media = (n1 + n2) / 2
        if media >= 6:
            print(f"Média: {media} - Aprovado")
        else:
            print(f"Média: {media} - Reprovado")  
   
