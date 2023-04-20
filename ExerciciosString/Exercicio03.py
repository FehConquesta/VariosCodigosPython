palavra = input("Digite uma palavra: ")
invertido = palavra[::-1]

if palavra == invertido:
    print("Palindromo")
else:
    print("Palavra normal")