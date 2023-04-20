numeros = []
par = []
impar = []
for i in range(10):
    numero =int(input("Informe um numero inteiro positivo: "))
    numeros.append(numero)
    if numero%2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(numeros)
print(par)
print(impar)