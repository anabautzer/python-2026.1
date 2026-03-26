import os
os.system ("cls")

# dado três valores e qual o valor intermediario

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if (n2 < n1 < n3) or (n3 < n1 < n2):
    intermediario = n1
elif (n1 < n2 < n3) or (n3 < n2 < n1):
    intermediario = n2
else:
    intermediario = n3

print(f"O valor intermediário é: {intermediario}") 