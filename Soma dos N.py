n = int(input("Digite o valor de n: "))
soma = 0.0
denominador = 1

for i in range(1, n + 1):
    termo = i / denominador
    print(f"{i}/{denominador} + ", end='')
    soma += termo
    denominador += 2

print(f"\nA soma da série é: {soma}")