numeros =[]
cont = 0
for i in range(10):
    numero = int(input(f"Digite o {i+1}° numero inteiro: "))
    numeros.append(numero)
    if numero % 3 == 0:
        cont +=1

print(f"Nesta lista tem {cont} multiplos de 3")