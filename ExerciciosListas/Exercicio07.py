lista = []
soma = 0
multi = 0
for i in range(5):
    lista.append(int(input("Digite um Numero: ")))

for i in range(len(lista)):
    soma += lista[i]
    if(i==0):
        multi = lista[i]
    else:
        multi *= lista[i]


print(lista)
print(f"A soma de todos os numeros é {soma}")
print(f"A multiplicação de cada valor pelo posterior é {multi}")