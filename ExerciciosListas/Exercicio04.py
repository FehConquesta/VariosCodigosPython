lista= []

consoantes = 0
for i in range(10):
    lista.append(input("Digite uma letra: "))

for i in range(len(lista)):
    if lista[i] in "AaEeIiOoUu":
        consoantes +=1

print(consoantes)