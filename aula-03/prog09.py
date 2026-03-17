import os
os.system ("cls")

# Caixa eletronico

num = float(input("Quantos dinheiros você gostaria de sacar: R$"))

resul50 = num // 50
resto50 = num  % 50
resul20 = resto50 // 20
resto20 = resul20 % 20
resul10 = resto20 // 10

print(f"Cédulas de 50: {resul50:.2f}")
print(f"Cédulas de 20: {resto20:.2f}")
print(f"Cédulas de 10: {resul10:.2f}")