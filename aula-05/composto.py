import os
os.system ("cls")

# dado o valor de uma compra, efetuar o desconto de 5% caso ela seja menor que R$ 1000,00 ou de 10% caso ela seja de ao menos R$ 1000,00

compra = float(input("Quanto foi gasto? "))
if compra < 1000.00:
    desconto = compra - (compra * 0.05) # desconto = compra * 0.95
else:
    desconto = compra - (compra * 0.10) # desconto = compra * 0.9, um jeito de resolver em precisar fazer a conta de menos

print(f"A compra foi de:  {compra:.2f} e o desconto de:  {desconto:.2f}")