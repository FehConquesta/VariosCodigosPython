maior = None
menor = None

while True:
    numero = int(input("Digite um número inteiro positivo (digite 0 para parar): "))
    if numero <= 0:
        break
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero


print(f"O maior número digitado foi {maior} e o menor número digitado foi {menor}.")