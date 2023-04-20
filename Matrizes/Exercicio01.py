matriz = []

for i in range(8):
    linha = []
    for j in range(6):
        linha.append(int(input(f"Digite um valor para [{i}][{j}] ")))
    matriz.append(linha)

print("Matriz formada")
for i in range(len(matriz)):
    print(matriz[i])


b = []

for linha in matriz:
    soma_linha = 0
    for valor in linha:
        soma_linha += valor
    b.append(soma_linha)

print("Lista formada com a soma das linhas:", b)
total = 0
for valor in b:
    total +=valor

print(f"Soma dos valores da lista B : {total}")
