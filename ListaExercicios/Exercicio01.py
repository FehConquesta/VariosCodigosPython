numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


maior_numero = max(numeros)
posicao = numeros.index(maior_numero)


print(f"O maior elemento é {maior_numero} e está na posição {posicao} da lista.")