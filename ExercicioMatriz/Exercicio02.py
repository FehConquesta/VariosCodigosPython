matriz = []
k = int(input("Informe um valor para multiplicar as diagonais "))
for i in range(3):
    linha= []
    for j in range(3):
        valor = int(input(f'Digite um numero [{i}][{j}]: '))
        if i == j:
            valor = valor * k

        linha.append(valor)

    matriz.append(linha)

dim = len(matriz)
for i in range(0,dim):
    print(matriz[i])
