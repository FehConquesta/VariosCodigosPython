frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
cont= 0

for letra in frase:
    if letra in vogais:
        cont +=1

print("A frase possui ", cont , " vogais")