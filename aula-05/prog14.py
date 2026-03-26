import os
os.system ("cls")

# dado três números e verificar qual é o maior

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 > n2 and n1 > n3:
    print(f"Maior valor: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"Maior valor: {n2}")  
elif n3 > n1 and n3 > n2:
    print(f"Maior valor: {n3}") 