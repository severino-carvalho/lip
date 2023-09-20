n = int(input())

L1 = []

for i in range(0, n):
    L1.append(input())

x = int(input())
y = int(input())


def selecionarIngredientes(ingrediente):
    if len(ingrediente) != x and len(ingrediente) != y:
        return ingrediente


print(list(filter(selecionarIngredientes, L1)))
