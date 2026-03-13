import os
os.system("cls")

nome1 = "Ana"
nome2 = "Carolina"
valor1 = 8450
valor2 = 45
valor3 = 45.96874
valor4 = 3455.456

# Formatações

print(f"Nome......: | {nome1:40s}| {nome2:40s}|") # faz 40 espaços
print(f"Nome......: | {nome1}| {nome2}|")
print(f"Nome......: | {nome2:40s}|")
print(f"Valor 1...: | {valor1: 7d}|") #7 espaços
print(f"Valor 1...: | {valor1: 07d}|") # 7 espaços + 2 zero
print(f"Valor 2...: | {valor2: 7d}|")
print(f"Valor 2...: | {valor2: 07d}|") # 7 espaços + 4 zero

print(f"Valor 3...: | {valor3:10.2f}|")
print(f"Valor 4...: | {valor4:10.2f}|")