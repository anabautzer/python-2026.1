import os
os.system ("cls")

# ordem cresente de 3 número

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 <= n2 and n1 <= n3:
    primeiro = n1
elif n2 <= n1 and n2 <= n3:
    primeiro = n2
else:
    primeiro = n3
if n1 >= n2 and n1 >= n3:
    terceiro = n1
elif n2 >= n1 and n2 >= n3:
    terceiro = n2
else:
    terceiro = n3
if (n1 != primeiro and n1 != terceiro):
    segundo = n1
elif (n2 != primeiro and n2 != terceiro):
    segundo = n2
else:
    segundo = n3

segundo = (n1 + n2 + n3) - primeiro - terceiro
print(f"Ordem crescente: {primeiro}, {segundo} e {terceiro}")