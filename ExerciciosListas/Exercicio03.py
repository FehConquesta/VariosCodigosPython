lista= []
soma = 0
for i in range(4):
    lista.append(float(input(f"Digite a nota {i}: ")))

for i in range(len(lista)):
    soma +=lista[i]


soma = soma/4
print(f"Suas notas foram {lista}")
print(f"A media do aluno é  {soma}")