#1. Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
#programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#• para homens: (72.7 * h) – 58;
#• para mulheres: (62.1 * h) – 44.7.
#ENTRADA
h = int(input("Qual a sua altura? em (centimetros)"))
s = input("Qual seu sexo? h=homem;m=mulher ")
#PROCESSAMENTO
if s == "h":
    p = 72.7 * (h/100) - 58
    print("Seu peso ideal é ", p)
else:
    p = 62.1 * (h/100) - 44.7
    print("Seu peso ideal é ", p)

