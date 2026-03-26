import os
os.system("cls")

# salario e inss

salario = float(input("Salário R$ "))

if salario <= 1518.00:
    inss = (salario*0.075) - 0
    print(f"INSS R$  {inss:.2f}")
elif salario >= 1518.01 and salario < 2793.88:
    inss = (salario * 0.09) - 22.77
    print(f"INSS R$ {inss:.2f}")
elif salario >= 2793.89 and salario < 4190.83:
    inss = (salario * 0.12) - 106.59
    print(f"INSS R$ {inss:.2f}")
else:
    inss = (8157.41 * 0.14) - 190.40
    print(f"INSS R$ {inss:.2f}")