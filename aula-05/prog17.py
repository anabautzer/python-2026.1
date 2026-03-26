import os
os.system ("cls")

# com três valores, se forma um triângulo

a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f"Os lados {a}, {b} e {c} formam um triângulo.")
else:
    print(f"Os lados {a}, {b} e {c} não formam um triângulo.")
      
