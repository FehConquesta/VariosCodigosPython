notas = []
soma = 0
quantidade = 0

while True:
    nota = float(input("Digite a nota (ou -1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)
    soma += nota
    quantidade += 1

if quantidade == 0:
    print("Nenhuma nota foi informada.")
else:
    media = soma / quantidade
    print("Quantidade de valores lidos:", quantidade)
    print("Soma dos valores:", soma)
    print("Média dos valores:", media)

    acima_da_media = 0
    abaixo_de_sete = 0
    for nota in notas:
        if nota > media:
            acima_da_media += 1
        if nota < 7:
            abaixo_de_sete += 1

    print("Quantidade de valores acima da média:", acima_da_media)
    print("Quantidade de valores abaixo de sete:", abaixo_de_sete)
