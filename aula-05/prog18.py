import os
os.system ("cls")

# com três valores, se forma um triângulo e os nomes

a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
       print(f"Os lados {a}, {b} e {c} formam um triângulo equilátero.")
    elif (a == b) or (a == c) or (b == c):
        print(f"Os lados {a}, {b} e {c} formam um triângulo isosceles.")
    elif a != b != c:
        print(f"Os lados {a}, {b} e {c} formam um triângulo escaleno.")
else:
    print(f"Os lados {a}, {b} e {c} não formam um triângulo.")
