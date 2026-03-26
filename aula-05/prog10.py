import os
os.system ("cls")

# descontro, acima de 100 - 10%, até 100 - 5%

compra = float(input("Compra: "))
if compra > 100:
    print("Você ganhou 10% de desconto!")
else:
    print("Você ganhou 5% de desconto!")    