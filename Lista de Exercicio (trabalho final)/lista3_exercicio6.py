#6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
#primeiro e último nome.
#ENTRADA
nomec = input("Digite seu nome completo: ")
#PROCESSAMENTO
nomep = ""
nomeu = ""

for i in range(len(nomec)):
    if nomec[i] == " ":
        nomep = nomec[:i]
        break

for i in range(len(nomec) - 1, -1, -1):
    if nomec[i] == " ":
        nomeu = nomec[i + 1:]
        break
print(nomep)
print(nomeu)