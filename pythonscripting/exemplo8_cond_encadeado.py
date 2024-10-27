#entrada
nota1 = float(input("digite nota 1: "))
nota2 = float(input("digite nota 2: "))
media = (nota1 + nota2) / 2
#processamento
if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("exame final")
else:
    print("Reprovado")
#saida