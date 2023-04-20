matriz = []
cont = 0
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        if(valor >10):
            cont +=1
    matriz.append(linha)

dim = len(matriz)
for i in range(0,dim):
    print(matriz[i])

print(f"Possui {cont} acima de 10")


