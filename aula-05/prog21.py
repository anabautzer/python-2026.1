import os
os.system("cls")

# imposto de renda + inss

salario = float(input("Salário R$ "))

if (salario <= 2259.20) or (salario <= 1518.00):
    inss = (salario*0.075) - 0
    ir = 0
    sl = salario - inss - ir
    print(f"INSS R$  {inss:.2f}")
    print(f"IR R$  {ir:.2f}")
    print(f"Salário líquido: {sl:.2f}")
elif (salario >= 2259.21 and salario < 2826.65) or (salario >= 1518.01 and salario < 2793.88):
    inss = (salario * 0.09) - 22.77
    ir = (salario * 0.075) - 169.44
    sl = salario - inss - ir
    print(f"INSS R$ {inss:.2f}")
    print(f"IR R$ {ir:.2f}")
    print(f"Salário líquido: {sl:.2f}")
elif (salario >= 2826.66 and salario < 3751.05) or (salario >= 2793.89 and salario < 4190.83):
    inss = (salario * 0.12) - 106.59
    ir = (salario * 0.15) - 381.44
    sl = salario - inss - ir
    print(f"INSS R$ {inss:.2f}")
    print(f"IR R$ {ir:.2f}")
    print(f"Salário líquido: {sl:.2f}")
elif (salario >= 3751.06 and salario < 4664.68):
    inss = (8157.41 * 0.14) - 190.40
    ir = (salario * 0.225) - 662.77
    sl = salario - inss - ir
    print(f"INSS R$ {inss:.2f}")
    print(f"IR R$ {ir:.2f}")
    print(f"Salário líquido: {sl:.2f}")
else:
    inss = (8157.41 * 0.14) - 190.40
    ir = (salario * 0.275) - 896.00
    sl = salario - inss - ir
    print(f"INSS R$ {inss:.2f}")
    print(f"IR R$ {ir:.2f}")
    print(f"Salário líquido: {sl:.2f}")