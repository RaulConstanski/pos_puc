## ENTRADA
NOME_PRODUTO = input("Digite o nome do seu produto: ")
PRECO = float(input("Digite o preço do seu produto: "))
QTD = int(input("Digite a quantidade do produto: "))

## PROCESSAMENTO
SUBTOTAL = PRECO * QTD
## SAÍDA
print("O nome do seu produto é: ",NOME_PRODUTO)
print(f"O preco do seu produto é: R$ {PRECO:.2f}")
print("A quantiadade do seu produto é: ",QTD)
print(f"O subtotal da sua compra é: R$ {SUBTOTAL:.2f}")

## o que é CRASHAR - fazer uma operação errada
## erro de EXECUÇÃO  - sintaxe
# variável = valor# variável recebe o valor# o valor é armazenado na variável# = é o operadr de atribuição#EntradaproductName = input("Digite o nome do seu produto: ") # texto variável (string)price = float(input("Digite o preço do produto: ")) # real variável (float)quantity = int(input("Digite a quantidade: ")) # inteiro variável (int)presente = input("Deseja embrulhar para presente? S/N ").lower()#Processamentosubtotal = price * quantity#Saídaprint("Produto:", productName)print("Preço: R$", price)print("Quantidade:", quantity)if presente == "S":    print("É para presente? Sim.")else:    print("É para presente? Não.")print("Total da compra: R$", subtotal)