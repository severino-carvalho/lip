n = int(input())
numeros = []

for _ in range(0, n):
    numeros.append(int(input()))

if numeros == sorted(numeros):
    print("ELEMENTOS ORDENADOS")
else:
    print("ELEMENTOS NÃO ORDENADOS")
