lista = []
par = []
impar = []

for i in range(20):
    lista.append(int(input("Digite um numero: ")))

for i in range(len(lista)):
    if(lista[i]%2 == 0):
        par.append(lista[i])
    else:
        impar.append(lista[i])

print(lista)
print(par)
print(impar)