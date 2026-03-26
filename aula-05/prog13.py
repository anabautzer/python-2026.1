import os
os.system ("cls")

# compra efetuada com 4 formar

compra = float(input("Compra: "))
escolha = int(input("Forma de pagamento (1 a 4): "))

if escolha == 1:
    pix = compra * 0.95
    print(f"Valor original R$ {compra:.2f}")
    print(f"Valor ajustado R$ {pix:.2f}")
elif escolha == 2:
    dinheiro = compra
    print(f"Valor original R$ {compra:.2f}")
    print(f"Valor ajustado R$ {dinheiro:.2f}")
elif escolha == 3:
    debito = compra * (1 + 0.01)
    print(f"Valor original R$ {compra:.2f}")
    print(f"Valor ajustado R$ {debito:.2f}")
elif escolha == 4:
    credito = compra * (1 + 0.025)
    print(f"Valor original R$ {compra:.2f}")
    print(f"Valor ajustado R$ {credito:.2f}")
