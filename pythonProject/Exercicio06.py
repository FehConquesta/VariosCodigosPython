senha = "1234"

while True:
    tentativa =input("Informe a senha: ")
    if (tentativa == senha):
        print("Parabens você acertou a senha:")
        break
    else:
        print("Senha incorreta tente novamente \n")
