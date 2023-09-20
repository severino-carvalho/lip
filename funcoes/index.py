# Usar as funções
# sort, sorted, min, max, sum, len, in, not in, count, index

vetor = [1, 8, 9, 5, 10, 74, 85, 2, 63]

# Ordenação modificando o vetor original
vetor_ordenado = vetor.sort()
vetor_reverso = vetor.sort(reverse=True)

# Ordenação sem modificar o vetor original
vetor_ordenado = sorted(vetor)
vetor_reverso = sorted(vetor, reverse=True)

# Mínimo e máximo
valor_minimo = min(vetor)
valor_maximo = max(vetor)

# Soma e média
soma_valores = sum(vetor)
media_valores = sum(vetor) / len(vetor)

# Tamanho do vetor
tamanho_vetor = len(vetor)

# Verificar se um valor existe ou não no vetor
vetor_contem_valor = 10 in vetor
vetor_nao_contem_valor = 10 not in vetor

# Contar quantas vezes um valor aparece no vetor
quantidade_valor = vetor.count(10)

# Verificar a posição de um valor no vetor
posicao_valor = vetor.index(10)

print("Valor")