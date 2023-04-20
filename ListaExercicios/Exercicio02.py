idades = []
menores_dezoito = 0
soma_idades = 0

idade = int(input("Digite a idade: "))
while idade >= 0:
    idades.append(idade)
    idade = int(input("Digite a idade: "))


for idade in idades:
    if idade < 18:
        menores_dezoito += 1
    soma_idades += idade

media_idades = soma_idades / len(idades)

print("Quantidade de usuários menores de 18 anos:", menores_dezoito)
print("Média das idades:", media_idades)