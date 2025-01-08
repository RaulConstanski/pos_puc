#7. Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
#de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
#Código de Exibição de Data
#• 1 – Data simples. Ex.: 10/08/1990;
#• 2 – Data abreviada. Ex.: 10/ago/1990;
#• 3 – Data completa. Ex.: 10 de agosto de 1990.
#ENTRADA
dia = int(input("Qual o dia da data do seu nascimento?: "))
mes = int(input("Qual o mês da data do seu nascimento?: "))
ano = int(input("Qual o ano da data do seu nascimento?: "))
forma = int(input("Qual o formato de data você deseja visualizar?\n1 – Data simples. Ex.: 10/08/1990\n2 – Data abreviada. Ex.: 10/ago/1990\n3 – Data completa. Ex.: 10 de agosto de 1990\nOpção: "))
if forma == 1:
    print(f"Sua data de nascimento é: {dia}/{mes}/{ano}")
elif forma == 2:
    if mes == 1:
        print(f"Sua data de nascimento é: {dia}/jan/{ano}")
    elif mes == 2:
        print(f"Sua data de nascimento é: {dia}/fev/{ano}")
    elif mes == 3:
        print(f"Sua data de nascimento é: {dia}/mar/{ano}")
    elif mes == 4:
        print(f"Sua data de nascimento é: {dia}/abr/{ano}")
    elif mes == 5:
        print(f"Sua data de nascimento é: {dia}/mai/{ano}")
    elif mes == 6:
        print(f"Sua data de nascimento é: {dia}/jun/{ano}")
    elif mes == 7:
        print(f"Sua data de nascimento é: {dia}/jul/{ano}")
    elif mes == 8:
        print(f"Sua data de nascimento é: {dia}/ago/{ano}")
    elif mes == 9:
        print(f"Sua data de nascimento é: {dia}/set/{ano}")
    elif mes == 10:
        print(f"Sua data de nascimento é: {dia}/out/{ano}")
    elif mes == 11:
        print(f"Sua data de nascimento é: {dia}/nov/{ano}")
    elif mes == 12:
        print(f"Sua data de nascimento é: {dia}/dez/{ano}")
elif forma == 3:
    if mes == 1:
        print(f"Sua data de nascimento é: {dia}/janeiro/{ano}")
    elif mes == 2:
        print(f"Sua data de nascimento é: {dia}/fevereiro/{ano}")
    elif mes == 3:
        print(f"Sua data de nascimento é: {dia}/março/{ano}")
    elif mes == 4:
        print(f"Sua data de nascimento é: {dia}/abril/{ano}")
    elif mes == 5:
        print(f"Sua data de nascimento é: {dia}/maio/{ano}")
    elif mes == 6:
        print(f"Sua data de nascimento é: {dia}/junho/{ano}")
    elif mes == 7:
        print(f"Sua data de nascimento é: {dia}/julho/{ano}")
    elif mes == 8:
        print(f"Sua data de nascimento é: {dia}/agosto/{ano}")
    elif mes == 9:
        print(f"Sua data de nascimento é: {dia}/setembro/{ano}")
    elif mes == 10:
        print(f"Sua data de nascimento é: {dia}/outubro/{ano}")
    elif mes == 11:
        print(f"Sua data de nascimento é: {dia}/novembro/{ano}")
    elif mes == 12:
        print(f"Sua data de nascimento é: {dia}/dezembro/{ano}")
else:
    print("Escolha inválida. Tente novamente.")