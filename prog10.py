import os
os.system ("cls")

# Próximo múltiplo de 5

num = int(input("Número: "))
resul = num + (5 - (num % 5))

print(f"O próximo multiplo de 5 a partir de {num} é {resul}")