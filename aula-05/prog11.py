import os
os.system ("cls")

# desconto de 7,5% caso ela seja acima de 5000 reias, se não calcular 3,5%

compra = float(input("Compra: "))

if compra > 5000:
    desconto = compra * 0.925
    print(f"Valor original R$ {compra:.2f}")
    print(f"Com desconto R$ {desconto:.2f}")
else:
    desconto = compra * 0.965
    print(f"Valor original R$ {compra:.2f}")
    print(f"Com desconto R$ {desconto:.2f}")
