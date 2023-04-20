impar = 0
par = 0
num1 = int(input("Informe um numero: "))
num2= int(input("Informe um numero maior que o anterior: "))
cont=num1
while(cont <= num2):
    if(cont%2 == 0):
        par = par +1
    else:
        impar = impar +1
    cont = cont +1
print(f"Entre os numeros {num1} e {num2}, tem {par} numeros pares e {impar} numeros impar")

