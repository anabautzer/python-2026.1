import os
os.system ("cls")

# número positivo, negativo e nulo

numero = int(input("Escreva um número: "))
if numero > 0:
    print(f"O número é positivo")
elif numero ==0:
    print(f"O número é nulo")
else:
    print(f"O número é negativo")