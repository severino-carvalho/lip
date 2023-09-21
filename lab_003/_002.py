n = int(input("Digite o valor de n: "))
nascimentos = []

for _ in range(n):
    nascimentos.append(int(input()))

soma_anterior = 0

for i in range(1, n):
    soma_anterior += nascimentos[i - 1]

    if nascimentos[i] > soma_anterior:
        print(f"dia {i}")
        break
    elif i == len(nascimentos) - 1:
        print("não há")
