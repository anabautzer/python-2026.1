import os
os.system("cls")

# imposto de renda

salario = float(input("Salário R$ "))

if salario <= 2259.20:
    ir = 0
    print(f"IR R$  {ir:.2f}")
elif salario >= 2259.21 and salario < 2826.65:
    ir = (salario * 0.075) - 169.44
    print(f"IR R$ {ir:.2f}")
elif salario >= 2826.66 and salario < 3751.05:
    ir = (salario * 0.15) - 381.44
    print(f"IR R$ {ir:.2f}")
elif salario >= 3751.06 and salario < 4664.68:
    ir = (salario * 0.225) - 662.77
    print(f"IR R$ {ir:.2f}")
else:
    ir = (salario * 0.275) - 896.00
    print(f"IR R$ {ir:.2f}")