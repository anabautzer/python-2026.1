import os
os.system("cls")

n1 = int(input("Digite um número: "))
cal = input("Sinal: ")
n2 = int(input("Digite um número: "))

match cal:
    case "+":
        soma = n1 + n2
        print(f"Resultado: {soma}")
    case "-":
        sub = n1 - n2
        print(f"Resultado: {sub}")
    case "*":
        mult = n1 * n2
        print(f"Resultado: {mult}")
    case "/":
        if n2 != 0:
            div = n1 / n2
            print(f"Resultado: {div}")
        else:
            print("Resultado: erro")
    case "//":
        if n2 != 0:
            div2 = n1 // n2
            print(f"Resultado: {div2}")
        else:
            print("Resultado: erro")    
    case "%":
        mod = n1 % n2
        print(f"Resultado: {mod}")
    case "**":
        exp = n1 ** n2
        print(f"Resultado: {exp}")              