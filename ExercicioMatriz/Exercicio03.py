matriz = []

for i in range(6):
    linha = []
    for j in range(3):
        valor = float(input(f"Informe um numero [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

dim = len(matriz)
maior = len(max(matriz))
print(maior)