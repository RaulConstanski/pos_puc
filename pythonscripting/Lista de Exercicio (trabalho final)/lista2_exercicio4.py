#4. Implemente um programa que calcule o que deve ser pago por um produto,
#considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
#os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
#cálculo adequado.
#Código Condição de pagamento
#• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
#• 2 – À vista no cartão de crédito, recebe 15% de desconto
#• 3 – Em duas vezes, preço normal de etiqueta sem juros
#• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%
#ENTRADA
produto = input("Qual produto está comprando? ")
preco = float(input("Qual valor do produto? "))
forma = int(input("Qual a forma de pagamento? escolha entre:\n1-À vista em dinheiro ou cheque, recebe 10% de desconto.\n2-À vista no cartão de crédito, recebe 15% de desconto.\n3-Em duas vezes, preço norma de etiqueta sem juros.\n4-Em duas vezes, preço normal de etiqueta mais juros de 10%\nForma:"))
#PROCESSAMENTO
if forma == 1:
    desconto = preco * 0.10
    preco = preco - desconto
    print(f"O desconto é de R$ {desconto} e o preço final é R$ {preco}.")
elif forma == 2:
    desconto = preco * 0.15
    preco = preco - desconto
    print(f"O desconto é de R$ {desconto} e o preço final é R$ {preco}.")
elif forma == 3:
    print(f"Serão duas parcelas de R${preco / 2}")
elif forma == 4:
    juros = preco * 0.10
    preco = preco + juros
    print(f"O juros é de R$ {juros} e o preço final é de R$ {preco}")
else:
    print("Opção de pagamento não disponível.")