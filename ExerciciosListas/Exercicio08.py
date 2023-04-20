idade =[]
altura = []

for i in range(2):
    idade.append(int(input("Digite a sua idade: ")))
    altura.append(float(input("Digite sua altura: ")))

idade = idade[::-1]
altura = altura [::-1]

print(idade)
print(altura)