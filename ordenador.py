def organizador(vetor):
    n = len(vetor)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

# Solicita ao usuário que insira os números separados por vírgulas
entrada_usuario = input("Digite os números a serem ordenados, separados por vírgulas seguindo o exemplo (*, *, *, *, *):")

# Converte a entrada do usuário em uma lista de inteiros
meu_vetor = [int(numero) for numero in entrada_usuario.split(',')]

print("Vetor antes da ordenação:", meu_vetor)

# Chama a função de ordenação
organizador(meu_vetor)

print("Vetor após a ordenação:", meu_vetor)
