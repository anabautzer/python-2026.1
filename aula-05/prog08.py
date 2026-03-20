import os
os.system ("cls")

# se a nota é valida

nota = float(input("Nota: "))
if 0 > nota or nota <= 10:
    print(f"{nota: .2f} é uma nota valida")
else:
    print(f"{nota: .2f} é uma nota invalida")