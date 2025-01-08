#Elaborar um algoritmo que solicita o nome de um produto, seu valor e
#quantidade, informando o valor de compra calculado
#ENTRADA
produto = input("Qual produto deseja calcular o total da compra? ")
vlr = float(input("Qual valor do produto? "))
qtd = int(input("Qual a quantidade comprada? "))
#PROCESSAMENTO
total = vlr * qtd
#SAIDA
print(f"O total da compra de {qtd} {produto} é {total}")