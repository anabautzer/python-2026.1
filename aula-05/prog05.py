import os
os.system ("cls")

# Próximo múltiplo de 5, se for ele, de o mesmo número

num = int(input("Número: "))
if num % 5 == 0:
    print(num)
else:
    resul = num + (5 - (num % 5))
    print(resul)