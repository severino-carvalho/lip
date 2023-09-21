n = int(input())
lista = []

for _ in range(0, n):
    lista.append(int(input()))

lista.reverse()

for i, value in enumerate(lista):
    if lista.count(value) > 1:
        del lista[i]

lista.reverse()
print(lista)
