import os
os.system ("cls")

# Média de 4 números pedindo com o usuário

num1 = float(input("Número 1: ")) # input com casting
num2 = input("Número 2: ") # vai receber como string
num2 = float(num2) # casting para mudar o tipo do dado
num3 = float(input("Número 3: "))
num4 = float(input("Número 4: "))
resul = (num1 + num2 + num3 + num4) / 4
print(f"A média de {num1}, {num2}, {num3} e {num4} é {resul:.2f}")