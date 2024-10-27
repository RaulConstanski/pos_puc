#5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
#(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
#Condição             Ida       Ida e volta
#Região Norte         R$ 500,00 R$ 900,00
#Região Nordeste      R$ 350,00 R$ 650,00
#Região Centro-Oeste  R$ 350,00 R$ 600,00
#Região Sul           R$ 300,00 R$ 550,00
regiao = int(input("Qual região você irá viajar?\n1=Região Norte\n2=Região Nordeste\n3=Região Centro-Oeste\n4=Região Sul\nOpção: "))
iv = int(input("Será apenas ida ou ida e volta:\n1=ida\n2=Volta\nOpção: "))
if regiao == 1 and iv == 1:
    print("O valor da sua viagem será de R$ 500",)
elif regiao == 1 and iv == 2:
    print("O valor da sua viagem será de R$ 900",)
elif regiao == 2 and iv == 1:
    print("O valor da sua viagem será de R$ 350",)
elif regiao == 2 and iv == 2:
    print("O valor da sua viagem será de R$ 650",)
elif regiao == 3 and iv == 1:
    print("O valor da sua viagem será de R$ 350",)
elif regiao == 3 and iv == 2:
    print("O valor da sua viagem será de R$ 600",)
elif regiao == 4 and iv == 1:
    print("O valor da sua viagem será de R$ 300",)
elif regiao == 4 and iv == 2:
    print("O valor da sua viagem será de R$ 550",)
else:
    print("Opção não reconhecida.")
SystemExit