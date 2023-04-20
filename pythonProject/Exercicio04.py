taxa_abatimento = float(input("Digite o percentual da taxa de abatimento: "))
prestacoes = int(input("Digite o numero de prestações: "))
valor_primeira = float(input("Informe o valor da primeira prestação: "))
cont = 1
valor_demais = valor_primeira

while(cont <= prestacoes):
    desconto = (valor_primeira *taxa_abatimento/100)
    valor_demais=valor_demais-desconto

    print(f"valor referente ao mes {cont} R${valor_demais:.2f}")

    cont = cont+1

