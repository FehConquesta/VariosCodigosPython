matriz = []
maior_linha = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Informe um valor [{i}][{j}]: "))
        linha.append(valor)

    valor_linha = sum(linha)

    matriz.append(linha)

print(valor_linha)


