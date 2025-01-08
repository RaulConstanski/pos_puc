#Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas
#4 notas bimestrais. O algoritmo deve calcular a média destas notas, e uma
#mensagem informando que a média da disciplina nome é média.
#ENTRADA
dis = input("Qual o nome da disciplina deseja saber sua média? ")
n1 = float(input("Qual foi sua nota no primeiro bimestre? (use ponto como separador decimal)"))
n2 = float(input("Qual foi sua nota no segundo bimestre? (use ponto como separador decimal)"))
n3 = float(input("Qual foi sua nota no terceiro bimestre? (use ponto como separador decimal)"))
n4 = float(input("Qual foi sua nota no quarto bimestre? (use ponto como separador decimal)"))
#PROCESSAMENTO
media = (n1 + n2 + n3 + n4) / 4
#SAIDA
print(f"A sua média na matéria {dis} foi de {media}")