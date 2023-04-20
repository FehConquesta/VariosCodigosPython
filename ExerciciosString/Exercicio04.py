data = input("Informe sua data de nascimento no formato dd/mm/aaaa:")

fragmento =data.split("/")

match fragmento[1]:
    case "01":
        print(fragmento[0], " de  Janeiro de ", fragmento[2])
    case "02":
        print(fragmento[0], " de  Fevereiro de ", fragmento[2])
    case "03":
        print(fragmento[0], " de  Março de ", fragmento[2])
    case "04":
        print(fragmento[0], " de  Abril de ", fragmento[2])
    case "05":
        print(fragmento[0], " de  Maio de ", fragmento[2])
    case "06":
        print(fragmento[0], " de  Junho de ", fragmento[2])
    case "07":
        print(fragmento[0], " de  Julho de ", fragmento[2])
    case "08":
        print(fragmento[0], " de  Agosto de ", fragmento[2])
    case "09":
        print(fragmento[0], " de  Setembro de ", fragmento[2])
    case "10":
        print(fragmento[0], " de  Outubro de ", fragmento[2])
    case "11":
        print(fragmento[0], " de  Novembro de ", fragmento[2])
    case "12":
        print(fragmento[0], " de  Dezembro de ", fragmento[2])

