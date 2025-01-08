#Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula
#sua idade com relação ao ano de 2020, sendo que o usuário já fez aniversário
#neste ano.
#ENTRADA
ano = int(input("Qual seu ano de nascimento? (em formato numeral)"))
#PROCESSAMENTO
ano = -ano + 2020
#SAIDA
print("Sua idade em 2020 após fazer aniversário era de: ",ano)