import os
os.system ("cls")

# venda, caso a venda seja acima de 100 mil, ele ganhará um bônus de 2 salários-fixos, se vender até 100 mil ele ganhará um bônus de 1,5 salário-fixo

salario = float(input("Salário-fixo: "))
venda = float(input("Venda do mês: "))
if venda > 100000:
    bonus = salario * 2
    print(f"Bônus de R$ {bonus:.2f}")
else:
    bonus = salario * 1.5
    print(f"Bônus de R$ {bonus:.2f}") 