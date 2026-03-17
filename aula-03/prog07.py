import os
os.system ("cls")

# Calculo de Km/L

km = float(input("Quantos quilomentros (KM) foram rodados: "))
lit = float(input("Quantos litros foram gastos: "))
resul = km / lit
print(f"O carro percorreu {km: .2f} quilometro com {lit: .2f} litros, rodando {resul: .2f} KM/L")