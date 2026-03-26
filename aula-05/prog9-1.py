import os
os.system("cls")

n1 = float(input("Nota 1: "))

if n1 < 0:
    print(f"A nota {n1:.2f} é invalida")
elif n1 > 10:
    print(f"A nota {n1:.2f} é invalida")
else:
    n2 = float(input("Nota 2: "))
    if n2 < 0:
        print(f"A nota {n2:.2f} é invalida")
    elif n2 > 10:
        print(f"A nota {n2:.2f} é invalida")
    else:
        media = (n1 + n2) / 2
        if media >= 6:
            print(f"Média: {media:.2f} - Aprovado")
        else:
            print(f"Média: {media:.2f} - Reprovado")   