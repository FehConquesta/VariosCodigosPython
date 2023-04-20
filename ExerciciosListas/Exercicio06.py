media =[]
cont = 0
for i in range(3):
    print(f"Aluno{i+1}")
    n1= float(input("Informe sua nota: "))
    n2 = float(input("Informe sua nota: "))
    n3 = float(input("Informe sua nota: "))
    n4 = float(input("Informe sua nota: "))
    print("")
    media.append((n1+n2+n3+n4)/4)


for i in range(len(media)):
    if(media[i]>7):
        cont +=1;


print(f"Foram {cont} que tiveram uma media acima de 7")
