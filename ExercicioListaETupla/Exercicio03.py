media = []
cont =0
for i in range(10):
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    n3 = float(input("Informe a terceira nota: "))
    print("")
    media.append((n1+n2+n3)/3)
    if media[i] >= 7:
        cont +=1

print("Foram ", cont, " alunos com media igual ou maior que 7")
