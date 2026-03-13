import os
os.system ("cls")

# Preço, cigarro e anos

num1 = float(input("Qual o preço do cigarro: "))
num2 = float(input("Quantos maços por dia: "))
num3 = int(input("Quantos anos fumando: "))
resul = (num1 * (num2 * 365)) * num3
print(f"Você gastou R${resul:.2f} fumando {num2} maços por dia, por {num3} anos")