#Estender o exercício 4 anterior informando que para pagamento à vista tem
#15% de desconto, calculando e exibindo este valor.
produto = input("Qual produto deseja calcular o total da compra? ")
vlr = float(input("Qual valor do produto? "))
qtd = int(input("Qual a quantidade comprada? "))
#PROCESSAMENTO
subtotal = vlr * qtd
desconto = subtotal * 0.15
total = subtotal - desconto
#SAIDA
print(f"O total da compra de {qtd} {produto} é:\nR$ {subtotal}; \npara pagamento a vista, possui desconto de:\nR$ {desconto} (15%)\ntotalzando em:\nR$ {total} a vista")