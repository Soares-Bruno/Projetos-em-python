base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1

if expoente < 0:
    base = 1 / base
    expoente = abs(expoente)

for _ in range(expoente):
    resultado *= base

print(f"O resultado de {base} elevado a {expoente} é: {resultado}")
